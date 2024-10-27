from django.urls import path
from .views import *
urlpatterns=[
    # path('product/add/',productadd),
    # path('products/',products),
    # path('product/delete/<int:id>/',productdelete,name = 'delete_product'),
    # path('product/update/<int:id>/',productupdate,name = 'update_product'),
    path('product/add/',Productadd.as_view()),
    path('products/',Products.as_view()),
    path('product/delete/<int:id>/',Product_delete.as_view(),name = 'delete_product'),
    path('product/update/<int:id>/',Product_update.as_view(),name = 'update_product'),
    
]