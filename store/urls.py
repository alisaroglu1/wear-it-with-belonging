from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('kategori/<slug:slug>/', views.category, name='category'),
    path('urun/<int:pk>/', views.product_detail, name='product_detail'),
    path('sepet/', views.cart_detail, name='cart_detail'),
    path('sepet/ekle/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('sepet/kaldir/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('siparis/', views.checkout, name='checkout'),
    path('siparis/onay/<int:pk>/', views.order_confirm, name='order_confirm'),
    path('profil/', views.profile, name='profile'),
    
]