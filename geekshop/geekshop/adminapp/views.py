from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCatAdminCreateForm, ProdAdminCreateForm
from authapp.models import User
from mainapp.models import Product, ProductCategories


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'title': 'Админка пользователи',
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Админка | Регистрация',
        'form': form
    }
    return render(request, 'adminapp/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Админка | Обновление пользователя',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))

@user_passes_test(lambda u: u.is_superuser)
def admin_product_categories(request):
    context = {
        'title': 'Geekshop | Категории товаров',
        'categories': ProductCategories.objects.all()
    }

    return render(request, 'adminapp/admin-product-categories-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_categories_create(request):
    if request.method == 'POST':
        form = ProductCatAdminCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_product_categories'))
        else:
            print(form.errors)
    else:
        form = ProductCatAdminCreateForm()
    context = {
        'title': 'Админка | Создание категорий продуктов',
        'form': form
    }
    return render(request, 'adminapp/admin-product-categories-create.html', context)




@user_passes_test(lambda u: u.is_superuser)
def admin_product_categories_update(request, id):
    product_cat_select = ProductCategories.objects.get(id=id)
    if request.method == 'POST':
        form = ProductCatAdminCreateForm(instance=product_cat_select, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрирвались')
            return HttpResponseRedirect(reverse('adminapp:admin_product_categories'))
        else:
            print(form.errors)
    else:
        form = ProductCatAdminCreateForm(instance=product_cat_select)
    context = {
        'title': 'Админка | Обновление категорий продуктов',
        'form': form,
        'product_cat_select': product_cat_select
    }
    return render(request, 'adminapp/admin-product-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_categories_delete(request, id):
    product_cat_select = ProductCategories.objects.get(id=id)
    product_cat_select.is_active = False
    product_cat_select.save()
    return HttpResponseRedirect(reverse('adminapp:admin_product_categories'))



@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    content = {'title': 'Geekshop | Товары',
               'products': Product.objects.all()
               }
    return render(request, 'adminapp/admin-products-read.html', content)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProdAdminCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products'))

        else:
            print(form.errors)
    else:
        form = ProdAdminCreateForm()
    content = {'title': 'Администратор | Создание продукта',
               'form': form}
    return render(request, 'adminapp/admin-products-create.html', content)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, id):
    prod_select = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProdAdminCreateForm(instance=prod_select, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно изменили продукт')
            return HttpResponseRedirect(reverse('adminapp:admin_products'))
        else:
            print(form.errors)
    else:
        form = ProdAdminCreateForm(instance=prod_select)
    content = {'title': 'Администратор | Редактирование товара',
               'form': form,
               'prod_select': prod_select}
    return render(request, 'adminapp/admin-products-update-delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, id):
    prod_select = Product.objects.get(id=id).delete()
    # # prod_cut_select.is_active = False
    # # prod_cut_select   .save()
    return HttpResponseRedirect(reverse('adminapp:admin_products'))