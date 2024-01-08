from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog, RegUser

class UserForm(ModelForm):
    class Meta:
        model = RegUser
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ( 'text',)
        widgets = {
            "text": forms.Textarea(attrs={'class':'form-control mb-2','rows':'5', 'placeholder': 'Post something!'}),
        }