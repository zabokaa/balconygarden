# Description: URL patterns for the products app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    # will contain the product id !
    path('<product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]
