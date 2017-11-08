from django.views import View
from django.shortcuts import render

from db.models import Category, Product, Unit


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
