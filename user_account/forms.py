from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile


# Form for user registration
class user_registration_form(UserCreationForm):
    # extending user creation form to include email
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Form for updating user informations
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Form for updating profile information
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']
