from django.shortcuts import render
import logging
from django.http import HttpResponse
from ht02app.models import Customer, Product, Order
from typing import List

logger = logging.getLogger(__name__)


def ht02(request):
    logger.info(f'{request} request received')
    return HttpResponse('ht02 page')


def customers(request):
    logger.info(f'{request} request received')
    customers = Customer.objects.all()
    return HttpResponse(customers)


def products(request):
    logger.info(f'{request} request received')
    products = Product.objects.all()
    return HttpResponse(products)


def orders(request):
    logger.info(f'{request} request received')
    orders = Order.objects.all()
    return HttpResponse(orders)
