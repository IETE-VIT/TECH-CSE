from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'landingpage.html')


def add_to_cart(request):
    return render(request, 'shoppingcart.html')


def profile(request):
    return render(request, 'profile.html')


def address(request):
    return render(request, 'addresses.html')


def orders(request):
    return render(request, 'orders.html')


def change_password(request):
    return render(request, 'changepass.html')


def login(request):
    return render(request, 'login.html')


def customerregistration(request):
    return render(request, 'register.html')


def checkout(request):
    return render(request, 'ordersummary.html')
