from django.urls import path
from .views import *
urlpatterns=[
    path('customer/add/',customeradd),
    path('customers/',customers),
    path('customer/delete/<int:id>/',customerdelete,name = 'delete_customer'),
    path('customer/update/<int:id>/',customerupdate,name = 'update_customer'),
    path('order/add/',orderadd),
    path('orders/',orders),
    path('order/delete/<int:id>/',orderdelete,name = 'delete_order'),
    path('order/update/<int:id>',orderupdate,name = 'update_order'),
    

]