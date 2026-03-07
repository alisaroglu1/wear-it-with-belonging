from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from store.models import Order, OrderItem, Product, Category
from django.db.models import Sum, Count


@staff_member_required
def dashboard_home(request):
    # Toplam satış
    total_revenue = Order.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0
    
    # Toplam sipariş
    total_orders = Order.objects.count()
    
    # Toplam ürün
    total_products = Product.objects.count()
    
    # Son 5 sipariş
    recent_orders = Order.objects.order_by('-created_at')[:5]
    
    # En çok satan ürünler
    top_products = OrderItem.objects.values(
        'product__name'
    ).annotate(
        total_sold=Sum('quantity')
    ).order_by('-total_sold')[:5]

    # Stok azalan ürünler
    low_stock = Product.objects.filter(stock__lte=5).order_by('stock')

    return render(request, 'dashboard/home.html', {
        'total_revenue': total_revenue,
        'total_orders': total_orders,
        'total_products': total_products,
        'recent_orders': recent_orders,
        'top_products': top_products,
        'low_stock': low_stock,
    })

@staff_member_required
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'dashboard/product_list.html', {
        'products': products
    })

@staff_member_required
def product_add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')
        is_active = request.POST.get('is_active') == 'on'

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            category_id=category_id,
            image=image,
            is_active=is_active
        )
        return redirect('dashboard:product_list')

    return render(request, 'dashboard/product_add.html', {
        'categories': categories
    })

@staff_member_required
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('dashboard:product_list')


@staff_member_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/category_list.html', {
        'categories': categories
    })

@staff_member_required
def category_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        Category.objects.create(name=name, slug=slug)
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/category_add.html')

@staff_member_required
def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('dashboard:category_list')


@staff_member_required
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'dashboard/order_list.html', {
        'orders': orders
    })


@staff_member_required
def order_delete(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect('dashboard:order_list')

@staff_member_required
def order_status_update(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.save()
    return redirect('dashboard:order_list')


@staff_member_required
def product_edit(request, pk):
    product = Product.objects.get(pk=pk)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.category_id = request.POST.get('category')
        product.is_active = request.POST.get('is_active') == 'on'
        
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        
        product.save()
        return redirect('dashboard:product_list')
    
    return render(request, 'dashboard/product_edit.html', {
        'product': product,
        'categories': categories
    })