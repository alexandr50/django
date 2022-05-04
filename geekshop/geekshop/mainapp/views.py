import json
import os
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from datetime import datetime
from mainapp.models import Product, ProductCategories
from django.views.generic import DetailView, TemplateView

now = datetime.today().strftime('%H:%M')
MODULE_DIR = os.path.dirname(__file__)

def read_json(file):
    file_path = os.path.join(MODULE_DIR, file)
    return json.load(open(file_path, encoding='utf-8'))


def index(request):
    content = {'title': 'GeekShop',
               'time': now}
    return render(request, 'mainapp/index.html', content)



def products(request, id_category=None, page=1):
    if id_category:
        products_ = Product.objects.filter(category_id=id_category)
    else:
        products_ = Product.objects.all()

    paginator = Paginator(products_, per_page=2)
    try:
        product_pagination = paginator.page(page)
    except PageNotAnInteger:
        product_pagination = paginator.page(1)
    except EmptyPage:
        product_pagination = paginator.page(paginator.num_pages)

    content = {'title': 'GeekShop - Каталог',
               'categories': ProductCategories.objects.all(),
               'products': product_pagination,
               'time': now}

    return render(request, 'mainapp/products.html', content)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'