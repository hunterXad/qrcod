from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your CustomUser model here


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required. Enter your last name.')
    email = forms.EmailField(
        max_length=254, required=True, help_text='Required. Enter your email address.')
    phone_number = forms.CharField(
        max_length=15, required=True, help_text='Required. Enter your phone number.')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email',
                  'phone_number', 'password1', 'password2']
        help_texts = {
            'password1': 'Your password must contain at least 8 characters.',
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }
        error_messages = {
            'email': {
                'unique': 'This email address is already registered.',
            },
        }
