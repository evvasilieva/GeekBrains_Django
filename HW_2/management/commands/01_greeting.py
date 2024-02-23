from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print 'It's the homework_02 after seminar_02!' to output."

    def handle(self, *args, **kwargs):
        self.stdout.write("It's the homework_02 after seminar_02!")
