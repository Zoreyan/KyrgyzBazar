from django.shortcuts import render, redirect
from .models import *

from django.contrib.auth.decorators import login_required
from django.db.models import F
from .filter import ShopFilter
from django.core.paginator import Paginator

# Shop List
def shop_list_view(request):
    shops = Shop.objects.all()

    search_input = request.GET.get('q') or ''
    if search_input:
        shops = Shop.objects.filter(title__icontains=search_input)
    myFilter = ShopFilter(request.GET, queryset=shops)
    
    if myFilter:
        shops = myFilter.qs
    else:
        shops = Shop.objects.all()

    context = {
        'shops': shops,
        'myFilter': myFilter,
    }
    return render(request, 'store/shop_list.html', context)

# Shop Detail
def shop_detail_view(request, pk):
    shop = Shop.objects.get(id=pk)
    products = Product.objects.filter(shop=shop)
    
    pictures = Pictures.objects.filter(shop=shop)
    custom_category = ProductCustomCategory.objects.filter(shop=shop)
    context = {
        'shop': shop,
        'pictures': pictures,
        'products': products,
        'custom_category': custom_category
    }
    return render(request, 'store/shop_detail.html', context)

# Shop List
def product_list_view(request):
    products = Product.objects.all()

    search_input = request.GET.get('prq') or ''

    if search_input:
        products = Product.objects.filter(title__icontains=search_input)

    context = {
        'products': products,
    }
    return render(request, 'store/product_list.html', context)