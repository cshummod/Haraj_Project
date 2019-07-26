from django import forms
from .models import Item


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
