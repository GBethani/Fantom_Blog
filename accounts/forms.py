from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(max_length=50)
    password2= forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile data.
    Uses ModelForm so Django handles validation & saving.
    """

    class Meta:
        model = UserProfile
        # Fields the user is allowed to update
        fields = ['birth_day', 'bio', 'image']

        # Optional: customize widgets (HTML attributes / styling)
        widgets = {
            'birth_day': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }
