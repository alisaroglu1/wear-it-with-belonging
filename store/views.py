from django.shortcuts import render
from .models import Product, Category

def home(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories
    })


def category(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category, is_active=True)
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'current_category': category
    })
