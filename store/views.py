from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from auth.models import CustomUser

from store.models import Order, Products

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/auth/login')
def dashboard(request):
    current_user = request.user
    return render(request, '_templates/pages/dashboards/index.html',{'current_user':current_user})


def about(request):
    current_user = request.user
    context = {'current_user':current_user}
    return render(request, '_templates/pages/dashboards/about.html',context)


def contact(request):
    current_user = request.user
    context = {'current_user':current_user}
    return render(request, '_templates/pages/dashboards/contact.html',context)

def shop(request):
    current_user = request.user
    product = Products.objects.all().values()
    context = {
    'product': product,'current_user':current_user}
    return render(request, '_templates/pages/dashboards/shop.html',context)

def shop_single(request, id):
    current_user = request.user
    print(current_user.id)
    if request.method == 'POST':
        product = request.POST.get('product-title')
        price = request.POST.get('product-price')
        quantity = request.POST.get('product-quanity')

        odr = Order(price=price,quantity=quantity, name = product, product_id = id, user_id = current_user.id)
        odr.save()
        

        return redirect('shop-single', id)

    else:

        prod = Products.objects.get(id=id)
        print(prod.name)
        context = {'prod': prod,'current_user':current_user}

        return render(request, '_templates/pages/dashboards/shop-single.html', context)

def orders(request, id):
    current_user = request.user
    odr = Order.objects.all().values()
    context = {
    'odr': odr, 'current_user':current_user}
    return render(request, '_templates/pages/dashboards/orders.html',context)