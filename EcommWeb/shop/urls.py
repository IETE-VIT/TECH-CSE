from django.contrib.auth.forms import PasswordResetForm
from shop.forms import Login_User
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import Login_User, Password_Change, Password_Reset, Password_Set, CustProfile_Info

urlpatterns = [

    path('', views.Prod_Available.as_view(), name='landingpage'),

    path('cart/', views.add_to_cart, name='shoppingcart'),

    path('displaycart/', views.display_cart, name='displaycart'),

    path('increase_cart/', views.add_item, name='itemadd'),

    path('decrease_cart/', views.decrease_item, name='itemred'),

    path('remove_cart/', views.remove_item, name='itemrem'),

    path('profile/', views.Cust_Profile.as_view(), name='profile'),

    path('address/', views.address, name='addresses'),

    path('orders/', views.orders, name='orders'),

    path('passwordsuccess/', views.passsuccess, name='passwordsuccess'),

    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='changepass.html',
         form_class=Password_Change, success_url='/passwordsuccess/'), name='changepass'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html',
         authentication_form=Login_User), name='login'),

    path('registration/', views.CustomerRegisterView.as_view(),
         name="register"),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=Password_Reset), name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=Password_Set), name='password_reset_confirm',),

    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('checkout/', views.checkout, name='ordersummary'),

    path('paymentdone/', views.payment_done, name='paymentdone'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
