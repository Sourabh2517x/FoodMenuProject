from django import forms
from django.contrib.auth.models import User  # --> user is inbuilt model of django
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:                             # --> Meta class hold the information of above form/class
        model = User                        # --> which model this form use
        fields = ['username','email','password1','password2']