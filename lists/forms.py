__author__ = 'sieg'

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email
from lists.models import *
import re

DUPLICATE_ITEM_ERROR = "Email is already in use."

class SignupForm(forms.models.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class RegistrationForm(forms.Form):
    username_ = forms.CharField(label='Username', max_length=100,
                             widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    fname_ = forms.CharField(label='First Name', max_length=100,
                             widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lname_ = forms.CharField(label='Last Name', max_length=100,
                             widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email_ = forms.EmailField(label='Email',
                              widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1_ = forms.CharField(label='Password',
                                 widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2_ = forms.CharField(label='Confirm Password',
                                 widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    def validate_password(self):
        if 'password1_' in self.cleaned_data:
            password1 = self.cleaned_data['password1_']
            password2 = self.cleaned_data['password2_']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def validate_username(self):
        username = self.cleaned_data['username_']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')

    def validate_email(self):
        email_ = self.cleaned_data['email_']
        if not validate_email(email_):
            raise forms.ValidationError('Invalid email format.')

    def save(self):
        data = self.cleaned_data

        user_ = User.objects.create(fname=data['fname_'],
                                    lname=data['lname_'],
                                    password=data['password1_'],
                                    email=data['email_'],
                                    username=data['username_']
                                    )
        user_.save()
        return user_
