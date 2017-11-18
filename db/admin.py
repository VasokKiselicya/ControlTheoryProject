from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

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
    list_display = ("name", "description", "small_preview",)
    search_fields = ("name",)
    readonly_fields = ("preview",)

    def small_preview(self, category):
        if category.photo:
            context = {"width": "100px", "source": category.photo, "extra_class": ""}
            return render_to_string("admin/preview.html", context=context)
        return ""
    small_preview.short_description = _('Small Preview')

    def preview(self, category):
        if category.photo:
            context = {"width": "100%", "source": category.photo, "extra_class": ""}
            return render_to_string("admin/preview.html", context=context)
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
    list_display = ("name", "short_name", "description")
    search_fields = ("name",)


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ("title", "lang", "created_at", "views", "header")
    readonly_fields = ('views', 'likes', 'dislikes')
    prepopulated_fields = {"slug": ("title",)}
    icon = '<i class="material-icons">forum</i>'


admin.site.unregister(Module)
