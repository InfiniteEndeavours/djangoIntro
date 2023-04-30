from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # Create a form that will allow us to add an item to the to do list
    class Meta:
        model = Item
        fields = ['name', 'done']
