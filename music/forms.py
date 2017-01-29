from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):# This is importing a user registration form
    password = forms.CharField(widget=forms.PasswordInput)
                                                           #This widget turns the typed in characters into ******
    
    class Meta: # class Meta is basically information about your class
        model = User  # User must be a forms class because i didn't make it
        fields = ["username", "email", "password"] 