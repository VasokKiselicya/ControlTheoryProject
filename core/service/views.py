import json
import os

from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from db.models import Category, Product, Unit, Article
from core.templatetags.app_tags import slugify
from core.service.cart import Cart
from core.service.forms import CartAddProductForm
from core.utils import DecimalEncoder


class MenuView(View):
    template_name = 'service/menu.html'

    def get(self, request):
        unit_names = dict(Unit.objects.all().values_list('id', 'short_name'))
        categories = list(Category.objects.all().values("id", "name", "description", "photo").order_by("order_no"))
        active_category = request.GET.get("category", "")
        for cat in categories:
            cat['slug'] = slugify(cat['name'])
            cat['active'] = cat['slug'] == active_category
            cat["products"] = list(Product.objects.filter(category_id=cat["id"]).order_by("name").values())
            for product in cat["products"]:
                product['unit_name'] = unit_names.get(product['unit_id'], '')
                # product["ingredients"] = ', '.join(Product.objects.get(id=product["id"]).product_ingredients.all()
                #                                    .values_list('ingredient__name', flat=True))
        if not active_category:
            categories[0].update({'active': True})
        return render(request, self.template_name, {"section": "menu", "categories": categories})


class ArticleView(View):
    template_name = 'blog/article.html'

    def get(self, request, slug):
        lang = get_language()
        article = Article.objects.filter(slug=slug).first()

        if article is None:
            raise Http404

        if article.lang != lang:
            another_article = Article.objects.filter(unique_name=article.unique_name, lang=lang).first()
            if another_article is not None:
                article = another_article

        article.views += 1
        article.save()

        return render(request, self.template_name, {'article': article})


class BlogView(View):
    template_name = 'blog/blog.html'

    def get(self, request):
        lang = get_language()
        articles = Article.objects.filter(lang=lang)
        if not articles.count():
            return render(request, self.template_name, {'error': 'articles_does_not_exists'})
        return render(request, self.template_name, {'articles': articles})


class RestaurantView(View):
    template_name = 'restaurant/restaurant.html'

    def get(self, request):
        root = os.path.join(settings.PROJECT_ROOT, 'static', 'images', 'slider')
        allfiles = [f'/static/images/slider/{f}' for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
        return render(request, self.template_name, {'files': json.dumps(allfiles).replace("'", "\'")})


class ContactsView(View):
    template_name = 'service/contacts.html'

    def get(self, request):
        return render(request, self.template_name, {})


class CartControl(View):

    @classmethod
    @csrf_exempt
    def get(cls, request):
        cart = Cart(request)
        return HttpResponse(json.dumps({"count": len(cart)}), content_type="application/json")

    @classmethod
    @csrf_exempt
    def post(cls, request):
        cart = Cart(request)
        request_body = json.loads(request.body.decode("utf-8") or "{}")
        product = get_object_or_404(Product, id=request_body.get('product_id', 0))

        form = CartAddProductForm(request_body)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'],
                     update_quantity=cd['update'])
            return HttpResponse(json.dumps({"count": len(cart)}), content_type="application/json")
        return HttpResponseBadRequest(json.dumps({'error': form.errors}), content_type="application/json")

    @classmethod
    @csrf_exempt
    def delete(cls, request):
        cart = Cart(request)
        request_body = json.loads(request.body.decode("utf-8") or "{}")
        product = get_object_or_404(Product, id=request_body.get('product_id'))
        cart.remove(product)
        return HttpResponse(json.dumps({"count": len(cart)}), content_type="application/json")


class CartView(View):
    template_name = 'service/basket.html'

    def get(self, request):
        return render(request, self.template_name)

    @classmethod
    def post(cls, request):
        cart = Cart(request)
        return HttpResponse(json.dumps({"basket": [x for x in cart]}, cls=DecimalEncoder),
                            content_type="application/json")


class CloseBasket(View):

    @classmethod
    @csrf_exempt
    def post(cls, request):
        body = json.loads(request.body.decode("utf-8") or "{}")
        cart = Cart(request)
        cart.save_to_db(request.user, **body)
        cart.clear()
        return HttpResponse(json.dumps({"success": True}), content_type="application/json")
