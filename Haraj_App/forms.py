from django import forms
from .models import Item, Profile
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile', 'gender']


class ItemForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Item
        fields = [
            'name',
            'category',
            'description',
            'picture',
            'price',
            'location',
            'mobile',
        ]
