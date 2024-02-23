from django.core.management.base import BaseCommand
from ht02app.models import Product


class Command(BaseCommand):
    help = "Update product amount by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('amount', type=int, help='Product amount')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        amount = kwargs.get('amount')
        product = Product.objects.filter(pk=pk).first()
        product.amount = amount
        product.save()
        self.stdout.write(f'{product}')
