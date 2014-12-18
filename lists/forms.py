__author__ = 'sieg'

from django import forms
from django.forms import ModelForm, PasswordInput
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from lists.models import *

DUPLICATE_ITEM_ERROR = "Email is already in use."

class RegistrationForm(forms.Form):
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

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def clean_email(self):
        email_ = self.cleaned_data['email']

        from django.core.validators import validate_email

        if not validate_email(email_):
            raise forms.ValidationError('Invalid email format.')
        try:
            User.objects.get(email=email_)
        except ObjectDoesNotExist:
            return email_
        raise forms.ValidationError('DUPLICATE_ITEM_ERROR')

    def save(self):
        data = self.cleaned_data

        user_ = User.objects.create(fname=data['fname'],
                                    lname=data['lname'],
                                    password=data['password1'],
                                    email=data['email'],
                                    )
        #user.save()
