from django import forms
from store.models import Item

class AddItemForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()

    class Meta:
        model = Item
        fields = {'title', 'description', 'price'}
