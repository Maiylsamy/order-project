from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .forms import *
#---------------------customer releated functions-------------------
@login_required(login_url='/')
def customeradd(request):
    context={
        'customer_form':Customer_form()
    }
    if request.method == 'POST':
        customer = Customer_form(request.POST)
        if customer.is_valid():
            customer.save()
    return render(request,'customer_add.html',context)

@login_required(login_url='/')
def customers(request):
    context= {
        'allcustomer' : Customer.objects.all()
    }
    return render(request,'customers.html',context)
@login_required(login_url='/')
def customerdelete(request,id):
    selected_customer = Customer.objects.get(id = id)
    selected_customer.delete()
    return redirect('/ordermanagement/customers/')
@login_required(login_url='/')
def customerupdate(request,id):
    selected_customer = Customer.objects.get(id = id)
    context = {
        'customer_form' : Customer_form(instance=selected_customer)
    }
    if request.method == 'POST':
        customer_update = Customer_form(request.POST,instance=selected_customer)
        if customer_update.is_valid():
            customer_update.save()
            return redirect('/ordermanagement/customers/')
    return render(request,'customer_add.html',context)

#---------------------order releated functions-------------------

def orderadd(request):
    context = {
        'order_form' : Order_form()
    }
    if request.method == 'POST':
        selected_product = Product.objects.get(id = request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        gst_amount = float(selected_product.gst * amount)/100
        total_amount = amount + gst_amount
        order = Order(Customer_reference_id = request.POST['Customer_reference'],product_reference_id= request.POST['product_reference'],order_number =request.POST['order_number'],order_date = request.POST['order_date'],quantity = request.POST['quantity'],price = amount,gst =gst_amount,bill = total_amount)
        order.save()
    return render(request,'order_add.html',context)

def orders(request):
    context = {
        'allorder' : Order.objects.all()
    }
    
    return render(request,'orders.html',context)

def orderdelete(request,id):
    selected_order = Order.objects.get(id = id)
    selected_order.delete()
    return redirect('/ordermanagement/orders/')

def orderupdate(request,id):
    selected_order = Order.objects.get(id = id)
    context = {
        'order_form' : Order_form(instance=selected_order)
    }
    if request.method == 'POST':
        selected_product = Product.objects.get(id = request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        gst_amount = float(selected_product.gst * amount)/100
        total_amount = amount + gst_amount
        order_filter = Order.objects.filter(id = id)
        order_filter.update(Customer_reference_id = request.POST['Customer_reference'],product_reference_id= request.POST['product_reference'],order_number =request.POST['order_number'],order_date = request.POST['order_date'],quantity = request.POST['quantity'],price = amount,gst =gst_amount,bill = total_amount)

        return redirect('/ordermanagement/orders/')
    
    return render(request,'order_add.html',context)    
    
