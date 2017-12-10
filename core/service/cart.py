from decimal import Decimal
from django.conf import settings
from db.models import Product, Order, OrderItem


class Cart(object):
    def __init__(self, request):

        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)

        if cart is None:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart

        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = list(Product.objects.filter(id__in=product_ids).values())
        for product in products:
            self.cart[str(product["id"])]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def save_to_db(self, user, **kwargs):
        order = Order.objects.create(user=user, address=kwargs.get("address", ""),
                                     phone_number=kwargs.get("phone", ""))
        order_items = []
        for product, item in self.cart.items():
            order_items.append(
                OrderItem(order=order, product_id=product,
                          quantity=item["quantity"], price=item["price"])
            )
        OrderItem.objects.bulk_create(order_items, batch_size=100)
