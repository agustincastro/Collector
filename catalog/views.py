from django.shortcuts import render
from django.views.generic import ListView


class CatalogListView(ListView):
    """
    Item results shown on index, this view handles pagination and rendering of the main page
    of the catalog app
    """
    queryset = []
    template_name = 'index.html'