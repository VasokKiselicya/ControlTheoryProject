from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location=settings.STATIC_ROOT)


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to='category_photos', null=True, storage=fs)

    class Meta:
        db_table = "category"
        verbose_name = _('Categories')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return self.__repr__()


class Unit(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=100)
    description = models.CharField(null=True, blank=True, max_length=300)

    class Meta:
        db_table = "unit"
        verbose_name = _('Units')
        verbose_name_plural = _('Units')
        ordering = ['name']

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return self.__repr__()


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='product_photos', null=True, storage=fs)
    description = models.TextField(null=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = "ingredient"
        verbose_name = _('Ingredients')
        verbose_name_plural = _('Ingredients')
        ordering = ['name']

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return self.__repr__()


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, related_name="products")
    photo = models.ImageField(upload_to='product_photos', null=True, storage=fs)
    price = models.DecimalField(null=False, decimal_places=2, max_digits=10, default=0)
    description = models.TextField(null=True)
    ingredients = models.ManyToManyField(Ingredient, through="ProductIngredients")
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = "product"
        verbose_name = _('Products')
        verbose_name_plural = _('Products')
        ordering = ['name']

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return self.__repr__()


class ProductIngredients(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.DecimalField(null=False, decimal_places=2, max_digits=10, default=0)

    class Meta:
        db_table = "product_ingredients"
        verbose_name = _('Product Ingredients')
        verbose_name_plural = _('Product Ingredients')
        unique_together = ("ingredient", "product")

    def __repr__(self):
        return '{} {}'.format(str(self.product), str(self.ingredient))

    def __str__(self):
        return self.__repr__()
