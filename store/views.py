from django.shortcuts import render,redirect
from .models import Product, Category, Cart, CartItem,Order,OrderItem,Profile
from django.contrib.auth.decorators import login_required


def home(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(is_active=True)
    
    if query:
        products = products.filter(name__icontains=query)
    
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'query': query
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


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'store/product_detail.html', {
        'product': product
    })

@login_required
def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += int(request.POST.get('quantity', 1))
        cart_item.save()
    
    return redirect('store:cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})

@login_required
def remove_from_cart(request, pk):
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(pk=pk, cart=cart)
    cart_item.delete()
    return redirect('store:cart_detail')


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=cart.total()
        )
        
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            item.product.stock -= item.quantity
            item.product.save()
        
        cart.items.all().delete()
        return redirect('store:order_confirm', pk=order.pk)
    
    return render(request, 'store/checkout.html', {'cart': cart})





@login_required
def order_confirm(request, pk):
    order = Order.objects.get(pk=pk, user=request.user)
    return render(request, 'store/order_confirm.html', {'order': order})


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile.phone = request.POST.get('phone', '')
        profile.address = request.POST.get('address', '')
        profile.city = request.POST.get('city', '')
        profile.district = request.POST.get('district', '')
        profile.zip_code = request.POST.get('zip_code', '')
        profile.save()
        return redirect('store:profile')
    
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'store/profile.html', {
        'profile': profile,
        'orders': orders
    })

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {
        'categories': categories
    })