from django.urls import path
from django.views.i18n import set_language
from adminapp.views import IndexTemplateView, UserListView, UserCreateView, UserUpdateView, \
    UserDeleteView, ProductCatListView, ProductCatCreateView, ProductCatUpdateView, ProductCatDeleteView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView

app_name = 'adminapp'
urlpatterns = [

    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user-create/', UserCreateView.as_view(), name='admin_user_create'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='admin_user_update'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_user_delete'),
    path('product-categories/', ProductCatListView.as_view(), name='admin_product_categories'),
    path('product-categories-create/', ProductCatCreateView.as_view(), name='admin_product_categories_create'),
    path('product-categories-update/<int:pk>/', ProductCatUpdateView.as_view(), name='admin_product_categories_update'),
    path('product-categories-delete/<int:pk>/', ProductCatDeleteView.as_view(), name='admin_product_categories_delete'),
    path('product/', ProductListView.as_view(), name='admin_products'),
    path('product-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('product-update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_products_delete'),
    path('lang/', set_language, name='set_language'),
]