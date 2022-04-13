from django.urls import path

from adminapp.views import admin_users, admin_user_update, admin_user_create, admin_user_delete, index, \
    admin_product_categories, admin_product_categories_create, admin_product_categories_update, \
    admin_product_categories_delete, admin_products, admin_products_create, admin_products_update, admin_products_delete

app_name = 'adminapp'
urlpatterns = [

    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('user-create/', admin_user_create, name='admin_user_create'),
    path('user-update/<int:id>/', admin_user_update, name='admin_user_update'),
    path('user-delete/<int:id>/', admin_user_delete, name='admin_user_delete'),
    path('product-categories/', admin_product_categories, name='admin_product_categories'),
    path('product-categories-create/', admin_product_categories_create, name='admin_product_categories_create'),
    path('product-categories-update/<int:id>/', admin_product_categories_update, name='admin_product_categories_update'),
    path('product-categories-delete/<int:id>/', admin_product_categories_delete, name='admin_product_categories_delete'),
    path('product/', admin_products, name='admin_products'),
    path('product-create/', admin_products_create, name='admin_products_create'),
    path('product-update/<int:id>/', admin_products_update, name='admin_products_update'),
    path('product-delete/<int:id>/', admin_products_delete, name='admin_products_delete')
]