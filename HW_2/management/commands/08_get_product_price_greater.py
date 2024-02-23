from django.core.management.base import BaseCommand
from ht02app.models import Product


class Command(BaseCommand):
    help = "Get product with price greater <price>."

    def add_arguments(self, parser):
        parser.add_argument('price', type=int, help='Product price')

    def handle(self, *args, **kwargs):
        price = kwargs['price']
        product = Product.objects.filter(price__gt=price)
        self.stdout.write(f'{product}')
