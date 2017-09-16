from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='category_photos', null=True)

    class Meta:
        db_table = "category"

    def __repr__(self):
        return '%s' % self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='product_photos', null=True)

    class Meta:
        db_table = "product"

    def __repr__(self):
        return '%s' % self.name
