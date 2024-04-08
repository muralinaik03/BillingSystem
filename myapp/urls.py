# urls.py (myapp)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/accounts/', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('main/', views.main_page, name='main_page'),
    path('home/', views.home, name='home'),
    path('add_bill/', views.add_bill, name='add_bill'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
]
