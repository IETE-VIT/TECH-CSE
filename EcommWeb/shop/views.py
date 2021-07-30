from django.shortcuts import render
from django.views import View
from .models import Customerdetails, Product, Cart, OrderDetails
from .forms import CustRegistration, CustProfile_Info
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'landingpage.html')


def add_to_cart(request):
    return render(request, 'shoppingcart.html')


def address(request):
    custadd = Customerdetails.objects.filter(user=request.user)
    return render(request, 'addresses.html', {'custadd': custadd})


def orders(request):
    return render(request, 'orders.html')


class CustomerRegisterView(View):
    def get(self, request):
        form = CustRegistration()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustRegistration(request.POST)
        if form.is_valid():
            messages.success(request, 'You have Registered Successfully!!')
            form.save()
        return render(request, 'register.html', {'form': form})


def checkout(request):
    return render(request, 'ordersummary.html')


def passsuccess(request):
    return render(request, 'passwordchanconfirm.html')


class Cust_Profile(View):
    def get(self, request):
        form = CustProfile_Info()
        return render(request, 'profile.html', {'form': form})

    def post(self, request):
        form = CustProfile_Info(request.POST)
        if form.is_valid():
            user = request.user
            Name = form.cleaned_data['Name']
            Address = form.cleaned_data['Address']
            City = form.cleaned_data['City']
            Pincode = form.cleaned_data['Pincode']
            State = form.cleaned_data['State']
            reg = Customerdetails(user=user,
                                  Name=Name, Address=Address, City=City, State=State, Pincode=Pincode)
            reg.save()

            messages.success(request, 'Address Has Been Added Successfully!!')
        return render(request, 'profile.html', {'form': form})
