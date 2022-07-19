from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {"all_products" : products}
    return render(request, 'store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(customer, order, type(order))
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_items" : 0, "get_cart_price": 0}
    context = {"items": items, "order" : order}
    return render(request, 'cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)