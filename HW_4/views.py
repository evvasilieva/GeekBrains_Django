# 📌 Измените модель продукта, добавьте поле для хранения фотографии продукта.
# 📌 Создайте форму, которая позволит сохранять фото.

import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import ProductFormWidget
from .models import Customer, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    """Отображает общую страницу проекта со всеми домашними заданиями"""
    logger.info(f'{request} request received')
    return render(request, 'index.html')


def ht04(request):
    """Отображает страницу для домашнего задания 4"""
    logger.info(f'{request} request received')
    return render(request, 'ht04app/ht04.html')


def get_customers(request):
    """Выводит список всех клиентов"""
    logger.info(f'{request} request received')
    customers = Customer.objects.all()
    context = {'title': 'Customers',
               'name': 'customer_orders',
               'items': customers}
    return render(request, 'ht04app/items.html', context)


def get_products(request):
    """Выводит список всех товаров"""
    logger.info(f'{request} request received')
    products = Product.objects.all()
    context = {'title': 'Products',
               'name': 'product_by_id',
               'items': products}
    return render(request, 'ht04app/items.html', context)


def orders(request):
    """Выводит список всех заказов"""
    logger.info(f'{request} request received')
    orders = Order.objects.all()
    context = {'title': 'Orders',
               'name': 'order_products',
               'items': orders}
    return render(request, 'ht04app/items.html', context)


def order_products(request, order_id):
    """Выводит список всех товаров в заказе по id"""
    order = get_object_or_404(Order, pk=order_id)
    products = Product.objects.filter(order=order).all()
    context = {'title': order.id,
               'list': 'Order',
               'items': products,
               'name': 'product_by_id'}
    return render(request, 'ht04app/item_by_id.html', context)


def customer_orders(request, customer_id):
    """Выводит список всех заказов клиента по id"""
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).all()
    context = {'title': customer.id,
               'list': 'Customer',
               'items': orders,
               'name': 'order_products'}
    return render(request, 'ht04app/item_by_id.html', context)


def product_by_id(request, product_id):
    """Выводит товар по id"""
    product = get_object_or_404(Product, pk=product_id)
    context = {'title': product.id,
               'list': 'Product',
               'product': product}
    return render(request, 'ht04app/product_by_id.html', context)


def customer_products(request, customer_id, period=7):
    """Выводит список всех товаров, заказанных клиентом по его id в указанный период"""
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer,
                                  date_ordered__gt=(timezone.now() - timezone.timedelta(days=period))).all()
    products = [product for order in orders for product in order.get_products.all()]
    context = {'title': customer.id,
               'list': 'Customer',
               'items': products,
               'name': 'order_products'}
    return render(request, 'ht04app/item_by_id.html', context)


def add_product_form(request):
    """Выводит форму добавления товара"""
    if request.method == 'POST':
        form = ProductFormWidget(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            date_added = form.cleaned_data['date_added']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            logger.info(f'Получили {title=}, {description=}, {price=}, {amount=},'
                        f'{date_added=}', f'фото загружено')
            product = Product(title=title, description=description, price=price,
                              amount=amount, date_added=date_added, image=image)
            product.save()
            message = 'Товар добавлен'
    else:
        form = ProductFormWidget()
        message = 'Заполните форму добавления товара'
    context = {'title': 'Форма товара',
               'form': form,
               'message': message,
               'name': 'add_product_form'}
    return render(request, 'ht04app/add_product_form.html', context)
