from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
from . import forms,models
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


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Allows a logged-in user to update their own profile.
    """

    model = models.UserProfile
    form_class = forms.UserProfileUpdateForm
    template_name = 'accounts/profile_update.html'

    # Redirect after successful update
    success_url = reverse_lazy('post-list')

    def get_object(self):
        """
        Ensures the user can ONLY edit their own profile.
        Prevents editing someone else's profile via URL manipulation.
        """
        return self.request.user.userprofile
    
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    """
    Allows a logged-in user to update their own profile.
    """

    model = models.UserProfile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        """
        Ensures the user can ONLY edit their own profile.
        Prevents editing someone else's profile via URL manipulation.
        """
        return self.request.user.userprofile

class PublicUserProfileView(DetailView):
    """
    Public-facing user profile view.
    """

    model = models.UserProfile
    template_name = 'accounts/public_profile.html'
    context_object_name = 'profile'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

