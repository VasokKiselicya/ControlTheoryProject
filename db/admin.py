from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django.utils.translation import ugettext as _

from db import models
from material.frontend.models import Module


class IngredientsStackedInline(admin.StackedInline):
    extra = 0
    fields = ('ingredient', 'weight')
    model = models.ProductIngredients

    class IngredientInlineFormset(forms.models.BaseInlineFormSet):

        def clean(self):
            super(IngredientsStackedInline.IngredientInlineFormset, self).clean()
            if not hasattr(self, 'cleaned_data'):
                return
            return self.cleaned_data

    formset = IngredientInlineFormset


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">free_breakfast</i>'
    list_display = ("name", "description", "photo",)
    search_fields = ("name",)
    readonly_fields = ("preview",)

    def preview(self, category):
        if category.photo:
            return format_html('<div class="col s12 center-align"><img src="/media/{}" width="100%" /></div>',
                               category.photo)
        return ""
    preview.short_description = _('Preview')


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">cake</i>'
    list_display = ("name", "category", "price", "description")
    search_fields = ("name",)
    inlines = [IngredientsStackedInline]


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">cake</i>'
    list_display = ("name", "description", "unit")
    search_fields = ("name",)


@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">cake</i>'
    list_display = ("name", "description")
    search_fields = ("name",)


admin.site.unregister(Module)
