from dataclasses import fields
from django import forms
from app1.models import Signup

class SignupForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Signup
        fields='__all__'      
        
class LoginForm(forms.ModelForm):          
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Signup
        fields=('Email','Password')
        
        
class UpdateForm(forms.ModelForm):          
    
    class Meta():
        model=Signup
        fields=('Name','Age','Place','Email','Photo')
        
class ChangepasswordForm(forms.Form):
    Oldpassword=forms.CharField(widget=forms.PasswordInput,max_length=8)
    Newpassword=forms.CharField(widget=forms.PasswordInput,max_length=8)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8)
    