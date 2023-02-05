from django import forms
from .models import UserModel, ProfileModel
from django.core.exceptions import ValidationError

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['user', 'created_at', 'updated_at']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
        }), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Password'
    }), label=False)


class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
        }), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Password'
    }), label=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Your Password'
    }), label=False)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user = UserModel.objects.get(username=username)
        if user:
            raise ValidationError(f'Ushbu {username} nomli username band!')
        return self.cleaned_data['username']
    
    def clean_confirm_password(self): 
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Parollar bir xil emas !')
        return self.cleaned_data['confirm_password']