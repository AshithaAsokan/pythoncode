from django.shortcuts import render, redirect
from .models import Product, Cart, Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Index view
def index(request):
    return render(request,'index.html')

@login_required
def home(request):
    ecomlist = Product.objects.all()
    return render(request, 'home.html', {'ecom': ecomlist})

def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'msg': 'Invalid login'})
    return render(request, 'login.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'sign_up.html', {'form': form, 'msg': 'Invalid signup details'})
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def addproduct(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Price = request.POST.get('price')
        Brand = request.POST.get('brand')
        Description = request.POST.get('description')

        if Name and Price and Brand and Description:
            Product.objects.create(name=Name, price=Price, brand=Brand, description=Description)
            return render(request, 'addproduct.html', {"msg": "Product added"})
        else:
            return render(request, 'addproduct.html', {"msg": "All fields are required."})
    return render(request, 'addproduct.html')

def display(request):
    ecomlist = Product.objects.all()
    return render(request, 'index.html', {'ecom': ecomlist})

@login_required
def delete(request):
    if request.method == 'POST':
        ecomname = request.POST.get('name')
        Product.objects.filter(name=ecomname).delete()
        return render(request, 'index.html', {'msg': 'Deleted'})
    return redirect('index')

@login_required
def updateprice(request):
    if request.method == 'POST':
        productname = request.POST.get('name')
        productbrand = request.POST.get('brand')
        oldprice = request.POST.get('oldprice')
        newprice = request.POST.get('newprice')
        ecomlist = Product.objects.filter(name=productname, brand=productbrand, price=oldprice)
        if ecomlist.exists():
            ecomlist.update(price=newprice)
            return render(request, 'index.html', {'msg': 'Updated the price'})
        else:
            return render(request, 'index.html', {'msg': 'No records found'})
    return redirect('index')

@login_required
def add_to_cart(request, productname):
    product = Product.objects.get(name=productname)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    cart_item.save()
    return redirect('home')

@login_required
def placeorder(request):
    # Check if the user is an admin
    if request.user.is_staff:
        # Handle status change when "Place Ship" is clicked
        if request.method == 'POST':
            order_id = request.POST.get('order_id')
            order = Order.objects.get(id=order_id)
            order.status = 'Shipped'
            order.save()
        
        # Fetch all orders
        orders = Order.objects.all()
        return render(request, 'placeorder.html', {'orders': orders})
    else:
        return redirect('home')
