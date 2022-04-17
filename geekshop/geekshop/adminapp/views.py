from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCatAdminCreateForm, ProdAdminCreateForm
from authapp.models import User
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import Product, ProductCategories
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, TemplateView, CreateView


# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'adminapp/admin.html')

class IndexTemplateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Главная страница'


# @user_passes_test(lambda u: u.is_superuser)
# # def admin_users(request):
# #     context = {
# #         'title': 'Админка пользователи',
# #         'users': User.objects.all()
# #     }
# #     return render(request, 'adminapp/admin-users-read.html', context)


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title = 'Админка пользователи'
    context_object_name = 'users'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'title': 'Админка | Регистрация',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-users-create.html', context)

class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title = 'Админка | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_update(request, id):
#     user_select = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#     context = {
#         'title': 'Админка | Обновление пользователя',
#         'form': form,
#         'user_select': user_select
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)

class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_users'))

class UserDeleteView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_users')


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_categories(request):
#     context = {
#         'title': 'Geekshop | Категории товаров',
#         'categories': ProductCategories.objects.all()
#     }

    # return render(request, 'adminapp/admin-product-categories-read.html', context)

class ProductCatListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-product-categories-read.html'
    title = 'Geekshop | Категории товаров'
    context_object_name = 'categories'



# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_categories_create(request):
#     if request.method == 'POST':
#         form = ProductCatAdminCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_product_categories'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductCatAdminCreateForm()
#     context = {
#         'title': 'Админка | Создание категорий продуктов',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-product-categories-create.html', context)

class ProductCatCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-product-categories-create.html'
    form_class = ProductCatAdminCreateForm
    title = 'Админка | Создание категорий продуктов'
    success_url = reverse_lazy('adminapp:admin_product_categories')



# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_categories_update(request, id):
#     product_cat_select = ProductCategories.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductCatAdminCreateForm(instance=product_cat_select, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрирвались')
#             return HttpResponseRedirect(reverse('adminapp:admin_product_categories'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductCatAdminCreateForm(instance=product_cat_select)
#     context = {
#         'title': 'Админка | Обновление категорий продуктов',
#         'form': form,
#         'product_cat_select': product_cat_select
#     }
#     return render(request, 'adminapp/admin-product-categories-update-delete.html', context)


class ProductCatUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-product-categories-update-delete.html'
    form_class = ProductCatAdminCreateForm
    title = 'Админка | Обновление категорий продуктов'
    success_url = reverse_lazy('adminapp:admin_product_categories')



# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_categories_delete(request, id):
#     product_cat_select = ProductCategories.objects.get(id=id)
#     product_cat_select.is_active = False
#     product_cat_select.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_product_categories'))

class ProductCatDeleteView(DeleteView, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = ProductCatAdminCreateForm
    success_url = reverse_lazy('adminapp:admin_product_categories')



    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



# @user_passes_test(lambda u: u.is_superuser)
# def admin_products(request):
#     content = {'title': 'Geekshop | Товары',
#                'products': Product.objects.all()
#                }
#     return render(request, 'adminapp/admin-products-read.html', content)

class ProductListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-read.html'
    title = 'Geekshop | Товары'
    context_object_name = 'products'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_create(request):
#     if request.method == 'POST':
#         form = ProdAdminCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#
#         else:
#             print(form.errors)
#     else:
#         form = ProdAdminCreateForm()
#     content = {'title': 'Администратор | Создание продукта',
#                'form': form}
#     return render(request, 'adminapp/admin-products-create.html', content)


class ProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = ProdAdminCreateForm
    title = 'Администратор | Создание продукта'
    success_url = reverse_lazy('adminapp:admin_products')

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_update(request, id):
#     prod_select = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProdAdminCreateForm(instance=prod_select, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно изменили продукт')
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#         else:
#             print(form.errors)
#     else:
#         form = ProdAdminCreateForm(instance=prod_select)
#     content = {'title': 'Администратор | Редактирование товара',
#                'form': form,
#                'prod_select': prod_select}
#     return render(request, 'adminapp/admin-products-update-delete.html', content)

class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProdAdminCreateForm
    title = 'Администратор | Редактирование товара'
    success_url = reverse_lazy('adminapp:admin_products')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_delete(request, id):
#     prod_select = Product.objects.get(id=id).delete()
#     # # prod_cut_select.is_active = False
#     # # prod_cut_select   .save()
#     return HttpResponseRedirect(reverse('adminapp:admin_products'))


class ProductDeleteView(DeleteView, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProdAdminCreateForm
    success_url = reverse_lazy('adminapp:admin_products')


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        # self.object.is_active = False if self.object.is_active else True
        # self.object.save()
        return HttpResponseRedirect(self.get_success_url())
