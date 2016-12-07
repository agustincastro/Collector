import datetime
from django import forms
from django.forms import ModelForm, DateInput
from django.forms.extras.widgets import SelectDateWidget
from catalog.models import Book


class ItemForm(ModelForm):
    date_aquired = forms.DateField(initial=datetime.date.today(), label="Date Aquired",
                                   # widget=DateInput(format='%Y-%m-%d'), input_formats=['%Y-%m-%d'])
                                   widget=SelectDateWidget)
    published_date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = Book
        fields = ['name', 'author', 'isbn', 'description', 'date_aquired', 'published_date', 'currency', 'price', 'quantity', 'category',
                  'thumbnail']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Some Name ...'}),
            'description': forms.Textarea(attrs={'rows': '4', 'placeholder': 'Item Description ...'}),
        }
