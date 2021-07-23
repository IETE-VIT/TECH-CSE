from django.urls import path
from shop import views

urlpatterns = [
    path('', views.home, name='landingpage'),
    path('cart/', views.add_to_cart, name='shoppingcart'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='addresses'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepass'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration,
         name='register'),
    path('checkout/', views.checkout, name='ordersummary'),
]
