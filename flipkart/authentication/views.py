from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/inventory/products/')
    if request.method == 'POST':
        user=authenticate(username=request.POST['user'],password = request.POST['password'])
        if user is not None :
            login(request,user)
            return redirect('/ordermanagement/customers/')
        else:
            context = {
                'error' : '* invalid user or password '
            }
            return render(request,'login.html',context)
    return render(request,'login.html') 

def logoutpage(request):
    logout(request)
    return redirect('/')

def signin(request):
    
    if request.method == 'POST':
        user_check = User.objects.filter(username = request.POST['user'])
        if len(user_check) > 0 :
            context = {
                'error' : ' ** user is already exist **'
            }
            return render(request,'signin.html',context)
        else:
                user = request.POST['user']
                firstname =request.POST['fname']
                lastname = request.POST['lname']
                email = request.POST['email']
                role = request.POST['role']
                new_user = User(username = user ,first_name = firstname,last_name = lastname ,email =email ,role = role )
                new_user.set_password( request.POST['password'])
                new_user.save()
                return redirect('/')
    return render(request,'signin.html')
