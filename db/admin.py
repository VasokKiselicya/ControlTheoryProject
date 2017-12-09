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


class OrderItemsStackedInline(admin.StackedInline):
    extra = 0
    fields = ('product', 'price', 'quantity')
    model = models.OrderItem
    readonly_fields = ['product', 'price', 'quantity']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


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
    icon = '<i class="material-icons">favorite</i>'
    list_display = ("name", "description", "unit")
    search_fields = ("name",)


@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">grade</i>'
    list_display = ("name", "short_name", "description")
    search_fields = ("name",)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">credit_card</i>'
    list_display = ("user", "address", "paid")
    search_fields = ("user", "address")
    # fields = ("user", "paid", "delivery_type", "address", "pay_method")
    readonly_fields = ["total_price"]
    exclude = ("id", )
    inlines = [OrderItemsStackedInline]

    def total_price(self, order):
        return "{:2f}".format(order.get_total_cost())

    total_price.short_description = _('Total Price')

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + list(set([field.name for field in self.opts.local_fields]) - {"id"})

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">forum</i>'
    list_display = ("title", "lang", "created_at", "views", "header")
    readonly_fields = ('views', 'likes', 'dislikes')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.ArticleName)
class ArticleNameAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">language</i>'
    list_display = ("name", "created_at")
    readonly_fields = ('created_at', 'updated_at')


@admin.register(models.TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    icon = ""
    list_display = ("full_name", "place_qty", "date")
    exclude = ("id",)

    def get_readonly_fields(self, request, obj=None):
        return list(set([field.name for field in self.opts.local_fields]) - {"id"})

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.unregister(Module)
