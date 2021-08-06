from itertools import product
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Customerdetails, Product, Cart, OrderDetails
from .forms import CustRegistration, CustProfile_Info, Login_User
from django.contrib import messages
from django.db.models import Q
# Create your views here.


class Prod_Available(View):
    def get(self, request):
        kitchen = Product.objects.filter(category='KC')
        kitchen_stockoff = Product.objects.filter(
            category='KC', stock_condition='OS')
        deo = Product.objects.filter(category='DEO')
        deo_stockoff = Product.objects.filter(
            category='DEO', stock_condition='OS')
        masala = Product.objects.filter(category='BM')
        masala_stockoff = Product.objects.filter(
            category='BM', stock_condition='OS')

        print(kitchen)
        productids = Product.objects.all()
        print(productids)

        print(product)

        iteminCart = False
        # iteminCart = Cart.objects.filter(
        #     Q(product=productids.id) & Q(user=request.user)).exists()
        print(iteminCart)
        return render(request, 'landingpage.html', {'kitchen': kitchen, 'deo': deo, 'masala': masala,
                                                    'kitchen_stockoff': kitchen_stockoff, 'deo_stockoff': deo_stockoff, 'masala_stockoff': masala_stockoff, 'iteminCart': iteminCart})


def add_to_cart(request):
    if request.user.is_authenticated:
        user = request.user
        proid = request.GET.get('pid')
        prod_id = Product.objects.get(id=proid)
        Cart(user=user, product=prod_id).save()
        return redirect('/displaycart')
    else:
        form = Login_User
        return render(request, 'login.html', {'form': form})


def display_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping = 60.0
        total = 0.0
        cart_products = [p for p in Cart.objects.all() if p.user ==
                         request.user]

        if cart_products:
            for p in cart_products:
                temp = (p.quantity * p.product.product_price)
                amount += temp
                if(amount >= 999.0):
                    shipping = 0.0
                else:
                    shipping = 60.0
                total = amount+shipping
            return render(request, 'shoppingcart.html', {'carts': cart, 'total': total, 'amount': amount, 'shipping': shipping})

        else:
            return render(request, 'emptycart.html')


def address(request):
    custadd = Customerdetails.objects.filter(user=request.user)
    return render(request, 'addresses.html', {'custadd': custadd})


def orders(request):
    order = OrderDetails.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orderplaced': order})


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


def add_item(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping = 60.0
        total = 0.0
        cart_products = [p for p in Cart.objects.all() if p.user ==
                         request.user]
        for p in cart_products:
            temp = (p.quantity * p.product.product_price)
            amount += temp
            if(amount >= 999.0):
                shipping = 0.0
            else:
                shipping = 60.0

        data = {'quantity': c.quantity, 'amount': amount,
                'total': amount+shipping}

        return JsonResponse(data)


def decrease_item(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping = 60.0
        total = 0.0
        cart_products = [p for p in Cart.objects.all() if p.user ==
                         request.user]
        for p in cart_products:
            temp = (p.quantity * p.product.product_price)
            amount += temp
            if(amount >= 999.0):
                shipping = 0.0
            else:
                shipping = 60.0

        data = {'quantity': c.quantity, 'amount': amount,
                'total': amount+shipping}

        return JsonResponse(data)


def remove_item(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping = 60.0
        total = 0.0
        cart_products = [p for p in Cart.objects.all() if p.user ==
                         request.user]
        for p in cart_products:
            temp = (p.quantity * p.product.product_price)
            amount += temp
            if(amount >= 999.0):
                shipping = 0.0
            else:
                shipping = 60.0

        data = {'amount': amount,
                'total': amount+shipping}

        return JsonResponse(data)


def checkout(request):
    user = request.user
    address = Customerdetails.objects.filter(user=user)
    items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping = 60.0
    total = 0.0
    cart_products = [p for p in Cart.objects.all() if p.user ==
                     request.user]
    if cart_products:
        for p in cart_products:
            temp = (p.quantity * p.product.product_price)
            amount += temp
            if(amount >= 999.0):
                shipping = 0.0
            else:
                shipping = 60.0
        total = amount+shipping
    return render(request, 'ordersummary.html', {'address': address, 'items': items, 'total': total})


def payment_done(request):
    user = request.user
    user_id = request.GET.get('user_id')
    customer = Customerdetails.objects.get(id=user_id)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderDetails(user=user, customer=customer,
                     product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")


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
