from django import forms
from .models import *
from django.contrib.auth.forms import *

class RegisterForm(forms.Form):
   username = forms.CharField(max_length=20, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
   email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
   password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class EventForm(forms.ModelForm):
    eventimages = forms.ImageField(label='Event Images',
                                   widget=forms.FileInput(attrs={'multiple': True,
                                                                          'class': 'button-create',
                                                                          }))
    publish_date = forms.DateTimeField(input_formats=['%d/%m'],
                                       label='Date',
                                       widget=forms.DateInput(attrs={'class': 'form-picker datepicker',
                                                                     'placeholder': 'DD/MM'}))
    season = forms.ModelChoiceField(queryset=Season.objects.all(), label='Seasons', empty_label="Choose season")

    class Meta:
        model = Event
        fields = ['name', 'text', 'season', 'account', 'publish_date', 'eventimages']


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'text',
                                                                            'placeholder': 'login'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'text email', 
                                                                           'placeholder': 'Email'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'text w3lpass',
                                                                              'placeholder': 'password'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'text w3lpass',
                                                                              'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save
        return user
    
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                 'placeholder': 'password'}))