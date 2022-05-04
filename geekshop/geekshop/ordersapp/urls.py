from django.urls import path
from ordersapp.views import OrderList, OrderRead, OrderCreate, OrderDelete, OrderUpdate, order_forming_complete

app_name = 'ordersapp'
urlpatterns = [

    path('', OrderList.as_view(), name='list'),
    path('read/<int:pk>/', OrderRead.as_view(), name='read'),
    path('create/', OrderCreate.as_view(), name='create'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('forming_complete/<int:pk>/', order_forming_complete, name='forming_complete'),

]
