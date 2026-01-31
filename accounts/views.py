from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
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

class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('users:password-change-done')

class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'accounts/change_password_done.html'


