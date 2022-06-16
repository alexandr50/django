import json

from chardet import detect
from django.core.management.base import BaseCommand

from authapp.models import User
from mainapp.models import ProductCategories, Product
def encoding_convert(file_name):
    """Конвертация"""
    with open(file_name, 'rb') as f_obj:
        content_bytes = f_obj.read()
    detected = detect(content_bytes)
    encoding = detected['encoding']
    content_text = content_bytes.decode(encoding)
    with open(file_name, 'w', encoding='utf-8') as f_obj:
        f_obj.write(content_text)



def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf8') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):

        User.objects.create_superuser(username='alex', email='alex@mail.ru', password='1')

        encoding_convert('mainapp/fixtures/cat.json')
        categories = load_from_json('mainapp/fixtures/cat.json')

        ProductCategories.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategories(**cat)
            new_category.save()
        encoding_convert('mainapp/fixtures/product.json')
        products = load_from_json('mainapp/fixtures/product.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ProductCategories.objects.get(id=category)
            prod['category'] = _category
            new_product = Product(**prod)
            new_product.save()

