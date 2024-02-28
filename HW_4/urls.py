from django.urls import path

from ht04app.views import ht04, get_customers, get_products, orders, \
    order_products, customer_orders, product_by_id, customer_products, \
    add_product_form

urlpatterns = [
    path('', ht04, name='ht04'),
    path('customers/', get_customers, name='customers'),
    path('products/', get_products, name='products'),
    path('orders/', orders, name='orders'),
    path('customers/<int:customer_id>', customer_orders, name='customer_orders'),
    path('customers/<int:customer_id>/products/', customer_products, name='customer_products'),
    path('products/<int:product_id>', product_by_id, name='product_by_id'),
    path('orders/<int:order_id>', order_products, name='order_products'),
    path('products/add', add_product_form, name='add_product_form'),
]
