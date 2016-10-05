import datetime
from django import forms
from catalog.models import Currency, Category


class ItemForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Some Name ...'}))
    description = forms.CharField(label='Description', max_length=500, widget=forms.Textarea( attrs={'rows':'4', 'placeholder': 'Item Description ...'}))
    isbn = forms.CharField(label='Isbn', max_length=13)
    date_aquired = forms.DateField(label='Date Aquired', initial=datetime.date.today())
    currency = forms.ModelChoiceField(label='Currency', queryset=Currency.objects.all())
    price = forms.IntegerField(label='Price', min_value=0)
    quantity = forms.IntegerField(label='Quantity', min_value=0, widget=forms.NumberInput)
    category = forms.ModelChoiceField(label='Category', queryset=Category.objects.all())
    thumbnail = forms.ImageField(label='Image')
