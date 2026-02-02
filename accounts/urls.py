from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogOutView.as_view(),name='logout'),
    path('password/edit/',views.ChangePasswordView.as_view(),name='password-change'),
    path('password/edit/done/',views.ChangePasswordDoneView.as_view(),name='password-change-done'),
    path('profile/edit/',views.UserProfileUpdateView.as_view(),name='profile-edit'),
    path('profile/',views.UserProfileDetailView.as_view(),name='profile'),
    path('<slug:slug>/',views.PublicUserProfileView.as_view(),name='public-profile'),
]