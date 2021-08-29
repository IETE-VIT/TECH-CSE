from django.forms.models import ModelForm
from shop.models import Customerdetails, ProductReview
from django import forms
from django.shortcuts import render
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserModel
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import messages
from django.contrib.auth import password_validation


class CustRegistration(UserCreationForm):
    password1 = forms.CharField(
        label='Create Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(
        required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'class': 'form-control'})}


class Login_User(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class Password_Change(PasswordChangeForm):
    old_password = forms.CharField(label=_("Enter Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label=_("Enter New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class Password_Reset(PasswordResetForm):
    email = forms.EmailField(label=_("Enter Your Email"), max_length=250, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))


class Password_Set(SetPasswordForm):
    new_password1 = forms.CharField(label=_("Enter New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class CustProfile_Info(forms.ModelForm):
    class Meta:
        model = Customerdetails
        fields = ['Name', 'Address', 'City', 'Pincode', 'State']
        widgets = {'Name': forms.TextInput(attrs={'class': 'form-control'}),
                   'Address': forms.TextInput(attrs={'class': 'form-control'}),
                   'City': forms.TextInput(attrs={'class': 'form-control'}),
                   'Pincode': forms.NumberInput(attrs={'class': 'form-control'}),
                   'State': forms.Select(attrs={'class': 'form-control'})}


class ProdReview(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['reviewer_name', 'review_title', 'review_detail', 'rating']
        widgets = {'reviewer_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'review_title': forms.TextInput(attrs={'class': 'form-control'}),
                   'review_detail': forms.Textarea(attrs={'class': 'form-control'}),
                   'rating': forms.Select(attrs={'class': 'form-control'})}
