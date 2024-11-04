from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def home(request):
    return render(request,'home.html')

def login_view(request):
    if request.method=='POST':
       uname=request.POST.get['username']
       pwd=request.POST.get['password']
       user=authenticate(request,username=uname,password=pwd)
       if user is not None:
          login(request,user)
          return redirect('home')
       else:
          return render(request,'login.html',{'msg':'Invalid login'})
    return render(request,'login.html')      
def sign_up(request):
    try:
     form=UserCreationForm(request.POST)
     if request.method=='POST':
        if form.is_valid():
             form.save()
             return redirect('login')
     else:
          return render(request,'sign_up.html',{'form':userform,'msg':'Invalid login'})  
    except Exception as e:
        print(e)
        userform=UserCreationForm()
        return render(request,'sign_up.html',{'form':userform})                      
    
def logout_view(request):
     logout(request)
     return redirect('login')

def addproduct(request):
    Name=request.POST['name']
    Price=request.POST['price']
    Brand=request.POST['brand']
    Description=request.POST['description']
    ecomlist=Product(name=Name,price=Price,brand=Brand,description=Description)
    ecomlist.save()
    return render(request,'index.html',{"msg":"Product added"})

def display(request):
    ecomlist=Product.objects.all()
    return render(request,'index.html',{'ecom':ecomlist})

def delete(request):
    ecomname=request.POST['name']
    ecomlist=Product.objects.filter(name=ecomname)
    ecomlist.delete()
    return render(request,'index.html',{'msg':'Deleted'}) 

def updateprice(request):
    productname=request.POST['name']
    productbrand=request.POST['brand']
    oldprice=request.POST['oldprice']
    newprice=request.POST['newprice']
    ecomlist= Product.objects.filter(name=productname,brand=productbrand,price=oldprice)
    if ecomlist.exists():
        ecomlist.update(price=newprice)
        return render(request,'index.html',{'msg':'Updated the price'})
    else:
        return render(request,'index.html',{'msg':'No records found'})