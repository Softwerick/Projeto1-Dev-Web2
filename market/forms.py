from django import forms
from . import models

class CreateUser(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'login', 'password', 'email']


class NewProduct(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'price', 'weight', 'storage', 'image']