from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from . import forms
# Create your views here.

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = forms.RegisterForm
    success_url = '/'
    
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserLogOutView(LogoutView):
    template_name = 'accounts/login.html'