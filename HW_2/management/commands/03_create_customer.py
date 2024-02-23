from django.core.management.base import BaseCommand
from ht02app.models import Customer


class Command(BaseCommand):
    help = "Create customer."

    def handle(self, *args, **kwargs):
        customer = Customer(name='Alex', email='alex@em.em', phone='+19991112233',
                            address='NY, 5th st, bld 5, apt 25')
        customer.save()
        self.stdout.write(f'{customer}')
