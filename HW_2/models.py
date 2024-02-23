# Задание No8
# 📌 Создайте три модели Django: клиент, товар и заказ. Клиент может иметь несколько заказов. Заказ может содержать
# несколько товаров. Товар может входить в несколько заказов.
# 📌 Поля модели "Клиент":
#   ○ имя клиента
#   ○ электронная почта клиента
#   ○ номер телефона клиента
#   ○ адрес клиента
#   ○ дата регистрации клиента
# 📌 Поля модели "Товар":
#   ○ название товара
#   ○ описание товара
#   ○ цена товара
#   ○ количество товара
#   ○ дата добавления товара
# 📌 Поля модели "Заказ":
#   ○ связь с моделью "Клиент", указывает на клиента,
# сделавшего заказ
#   ○ связь с моделью "Товар", указывает на товары, входящие в заказ
#   ○ общая сумма заказа
#   ○ дата оформления заказа
# 📌 *Допишите несколько функций CRUD для работы с моделями по желанию.
# Что по вашему мнению актуально в такой базе данных.
from django.db import models
from typing import List


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.email}, {self.phone}    '


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}: {self.price}ye x {self.amount}шт     '


class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.name}: {list(map(str, self.products.all()))} = {self.total_price}ye     '
