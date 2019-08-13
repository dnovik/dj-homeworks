import csv
from datetime import datetime
from slugify import slugify

from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                unit = Phone()
                unit.uid = line[0]
                unit.name = line[1]
                unit.image = line[2]
                unit.price = line[3]
                unit.release_date = datetime.date(datetime.strptime(line[4], "%Y-%m-%d"))
                unit.lte_exists = line[5]
                unit.slug = slugify(unit.name)
                unit.save()
