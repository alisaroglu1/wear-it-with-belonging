from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('urunler/', views.product_list, name='product_list'),
    path('urun/ekle/', views.product_add, name='product_add'),
    path('urun/sil/<int:pk>/', views.product_delete, name='product_delete'),
    path('kategoriler/', views.category_list, name='category_list'),
    path('kategori/ekle/', views.category_add, name='category_add'),
    path('kategori/sil/<int:pk>/', views.category_delete, name='category_delete'),
    path('siparisler/', views.order_list, name='order_list'),
    path('siparis/sil/<int:pk>/', views.order_delete, name='order_delete'),
    path('siparis/durum/<int:pk>/', views.order_status_update, name='order_status_update'),
    path('urun/duzenle/<int:pk>/', views.product_edit, name='product_edit'),
]