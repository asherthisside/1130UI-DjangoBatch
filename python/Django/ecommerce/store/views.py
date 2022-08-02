from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(customer, order, type(order))
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_items" : 0, "get_cart_price": 0}
    products = Product.objects.all()
    context = {"all_products" : products, "order":order}
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
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(customer, order, type(order))
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_items" : 0, "get_cart_price": 0}
    context = {"items": items, "order" : order}
    return render(request, 'checkout.html', context)


def update_cart(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    print(product_id, action)

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer = customer, complete= False)
    product = Product.objects.get(id=product_id)

    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderitem.quantity += 1
    else:
        orderitem.quantity -= 1 

    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()


    return JsonResponse("Item was added", safe=False)