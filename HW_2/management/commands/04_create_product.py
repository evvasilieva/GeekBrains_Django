from django.core.management.base import BaseCommand
from ht02app.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(title='product', description='', price=64_999.99, amount=20)
        product.save()
        self.stdout.write(f'{product}')
