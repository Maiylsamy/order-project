from django.shortcuts import render ,redirect
from .forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
#---------------------product releated functions-------------------

# Create your views here.
# def productadd(request):
#     context={
#         'product_form':Product_form()
#     }
#     if request.method == 'POST':
#         product = Product_form(request.POST)
#         if product.is_valid():
#             product.save()
#     return render(request,'product_add.html',context)

# def products(request):
#     context= {
#         'allproduct' : Product.objects.all()
#     }
#     return render(request,'products.html',context)

# def productdelete(request,id):
#     selected_product = Product.objects.get(id = id)
#     selected_product.delete()
#     return redirect('/inventory/products/')

# def productupdate(request,id):
#     selected_product = Product.objects.get(id = id)
#     context = {
#         'product_form' : Product_form(instance=selected_product)
#     }
#     if request.method == 'POST':
#         product_update = Product_form(request.POST,instance=selected_product)
#         if product_update.is_valid():
#             product_update.save()
#             return redirect('/inventory/products/')
#     return render(request,'product_add.html',context)

# =================create class for views=================

class Productadd(LoginRequiredMixin,View):
    login_url='/'
    def get(self,request):
        context={
            'product_form':Product_form()
         }
        return render(request,'product_add.html',context)
    
    def post(self,request):
        product = Product_form(request.POST)
        if product.is_valid():
            product.save()
        return redirect('/inventory/products/')

class Products(LoginRequiredMixin,View):
    login_url='/'
    def get(self,request):
        context= {
        'allproduct' : Product.objects.all()
        }
        return render(request,'products.html',context)
    
class Product_delete(LoginRequiredMixin,View):
    login_url='/'
    def get(self,request,id):
        selected_product = Product.objects.get(id = id)
        selected_product.delete()
        return redirect('/inventory/products/')
    
class Product_update(LoginRequiredMixin,View):
    login_url='/'
    def get(self,request,id):
        selected_product = Product.objects.get(id = id)
        context = {
        'product_form' : Product_form(instance=selected_product)
        }
        
        return render(request,'product_add.html',context)
        
    def post(self,request,id):
        selected_product = Product.objects.get(id = id)
        product_update = Product_form(request.POST,instance=selected_product)
        if product_update.is_valid():
            product_update.save()
            return redirect('/inventory/products/')