from django.views import View
from django.shortcuts import render
from django.utils.translation import get_language
from db.models import Category, Product, Unit, Article
from core.templatetags.app_tags import slugify


class MenuView(View):
    template_name = 'service/menu.html'

    def get(self, request):
        unit_names = dict(Unit.objects.all().values_list('id', 'short_name'))
        categories = list(Category.objects.all().values("id", "name", "description", "photo").order_by("id"))
        active_category = request.GET.get("category", "")
        for cat in categories:
            cat['slug'] = slugify(cat['name'])
            cat['active'] = cat['slug'] == active_category
            cat["products"] = list(Product.objects.filter(category_id=cat["id"]).order_by("name").values())
            for product in cat["products"]:
                product['unit_name'] = unit_names.get(product['unit_id'], '')
                product["ingredients"] = ', '.join(Product.objects.get(id=product["id"]).product_ingredients.all()
                                                   .values_list('ingredient__name', flat=True))
        if not active_category:
            categories[0].update({'active': True})
        return render(request, self.template_name, {"section": "menu", "categories": categories})


class ArticleView(View):
    template_name = 'blog/article.html'

    def get(self, request, slug):
        lang = get_language()
        article = Article.objects.filter(slug=slug, lang=lang).first()
        if article is None:
            return render(request, self.template_name, {'error': 'article_not_exists'} )
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
    template_name = 'blog/blog.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ContactsView(View):
    template_name = 'blog/blog.html'

    def get(self, request):
        return render(request, self.template_name, {})
