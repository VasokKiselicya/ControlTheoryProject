from django.views import View
from django.shortcuts import render
from django.utils.translation import get_language
from db.models import Category, Product, Unit, Article


class MenuView(View):
    template_name = 'service/menu.html'

    def get(self, request):
        unit_names = dict(Unit.objects.all().values_list('id', 'short_name'))
        categories = list(Category.objects.all().values("id", "name", "description", "photo").order_by("id"))
        for cat in categories:
            cat["products"] = list(Product.objects.filter(category_id=cat["id"]).order_by("name").values())
            for product in cat["products"]:
                product['unit_name'] = unit_names.get(product['unit_id'], '')
                product["ingredients"] = ', '.join(Product.objects.get(id=product["id"]).product_ingredients.all()
                                                   .values_list('ingredient__name', flat=True))
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


