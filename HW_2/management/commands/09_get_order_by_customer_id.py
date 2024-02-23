from django.core.management.base import BaseCommand
from ht02app.models import Order


class Command(BaseCommand):
    help = "Get all orders by customer id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        orders = Order.objects.filter(customer__pk=pk).all()
        for order in orders:
            self.stdout.write(f'{order}')
