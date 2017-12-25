from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


fs = FileSystemStorage(location=settings.UPLOAD_PATH)


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name=_("Category Name"))
    description = models.TextField(null=True, verbose_name=_("Description"))
    photo = models.ImageField(upload_to='category_photos', null=True, storage=fs, verbose_name=_("Image"))
    order_no = models.PositiveIntegerField(null=False, unique=True, verbose_name=_("Order Number"))

    class Meta:
        db_table = "category"
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return self.__repr__()


class Unit(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=100, verbose_name=_("Unit Name"))
    description = models.CharField(null=True, blank=True, max_length=300, verbose_name=_("Description"))
    short_name = models.CharField(null=False, blank=False, max_length=10, unique=True, verbose_name=_("Short Value"))

    class Meta:
        db_table = "unit"
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')
        ordering = ['name']

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return self.__repr__()


class Ingredient(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Ingredient Name"), blank=False, null=False)
    photo = models.ImageField(upload_to='ingredient_photos', null=True, storage=fs,
                              default='ingredient_photos/not_found_404.png', verbose_name=_("Image"), blank=True)
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=False, verbose_name=_("Unit"))

    class Meta:
        db_table = "ingredient"
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')
        ordering = ['name']

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return self.__repr__()


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, unique=True, verbose_name=_("Product Name"))
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT,
                                 related_name="products", verbose_name=_("Category"))
    photo = models.ImageField(upload_to='product_photos', null=True, storage=fs, verbose_name=_("Image"))
    price = models.DecimalField(null=False, decimal_places=2, max_digits=10, default=0, verbose_name=_("Price"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    ingredients = models.ManyToManyField(Ingredient, through="ProductIngredients", verbose_name=_("Ingredients"))
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=False, verbose_name=_("Unit"))
    weight = models.DecimalField(null=False, decimal_places=3, max_digits=10, default=0, verbose_name=_("Weight"))

    class Meta:
        db_table = "product"
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['name']

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return self.__repr__()


class ProductIngredients(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name=_("Ingredient"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_ingredients', verbose_name=_("Product"))
    weight = models.DecimalField(null=False, decimal_places=3, max_digits=10, default=0, verbose_name=_("Weight"))

    class Meta:
        db_table = "product_ingredients"
        verbose_name = _('Product Ingredients')
        verbose_name_plural = _('Product Ingredients')
        unique_together = ("ingredient", "product")

    def __repr__(self):
        return '{} {}'.format(str(self.product), str(self.ingredient))

    def __str__(self):
        return self.__repr__()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name=_("User"))
    address = models.CharField(verbose_name=_('Address'), max_length=250)
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=25)
    created_at = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)
    paid = models.BooleanField(verbose_name=_('Paid'), default=False)

    class Meta:
        db_table = "order"
        ordering = ('-created_at', )
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return '{}: {}'.format(_("Order"), self.id)

    __repr__ = __str__

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items', verbose_name=_("Product"))
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"), default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def __repr__(self):
        return self.__str__()

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        db_table = "order_item"
        ordering = ('product', )
        verbose_name = _('OrderItem')
        verbose_name_plural = _('OrderItems')


class ArticleName(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)
    name = models.CharField(max_length=200, unique=True, blank=False, null=False,
                            verbose_name=_("Unique Article Name"), default="")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        ordering = ['-id']
        verbose_name = _("Article Identifier")
        verbose_name_plural = _("Articles Identifiers")
        db_table = "vincent_article_name"


class Article(models.Model):
    unique_name = models.ForeignKey(ArticleName, on_delete=models.CASCADE, null=False,
                                    verbose_name=_("Article Identifier"))
    title = models.CharField(max_length=200, verbose_name=_("Article Title"), blank=False, null=False)
    header = models.TextField(verbose_name=_("Card Article Preview"))
    slug = models.SlugField(max_length=200, unique=True, blank=False, verbose_name=_("Unique Article Identifier"))
    image = models.ImageField(upload_to='article_images', storage=fs,
                              max_length=200, null=False, verbose_name=_("Article Image"))
    lang = models.CharField(max_length=20, choices=settings.LANGUAGES, default='uk', verbose_name=_("Language"))
    body = RichTextField(verbose_name=_("Article Body"), null=False, blank=False)
    created_at = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)
    views = models.PositiveIntegerField(default=0, verbose_name=_("Views Count"))
    likes = models.PositiveIntegerField(default=0, verbose_name=_("Likes Count"))
    dislikes = models.PositiveIntegerField(default=0, verbose_name=_("Dislikes Count"))

    def __str__(self):
        return '{} [{}]'.format(self.title, self.lang)

    __repr__ = __str__

    class Meta:
        db_table = "vincent_articles"
        ordering = ('-created_at', )
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        unique_together = (("unique_name", "lang"),)


class TableBooking(models.Model):
    full_name = models.CharField(max_length=300, blank=False, null=False, verbose_name=_("Full Name"))
    place_qty = models.IntegerField(default=2, verbose_name=_("Places Quantity"))
    date = models.DateTimeField(verbose_name=_("Booking Date"))
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=25)
    wish = models.TextField(blank=True, default="", null=False, max_length=300, verbose_name=_("User Wish"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name=_("User"))
    created_at = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)

    class Meta:
        db_table = "table_booking"
        ordering = ('-created_at', )
        verbose_name = _('TableBooking')
        verbose_name_plural = _('Bookings')

    def __str__(self):
        return '{} => {} [{}]'.format(self.full_name, self.place_qty,
                                      self.date.strftime("%Y-%m-%d %H:%M"))

    __repr__ = __str__
