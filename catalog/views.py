from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Collector import settings
from catalog.models import Book


class Index(ListView):
    """
    Item results shown on index, this view handles pagination and rendering of the main page
    of the catalog app
    """
    model = Book
    template_name = 'index.html'
    paginate_by = settings.PAGER_TAKE

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        items = Book.objects.all()

        page = self.request.GET.get('page')
        #Add range template context variable that we can loop through pages
        context['range'] = range(context['paginator'].num_pages)
        paginator = Paginator(items, self.paginate_by)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context['items'] = items
        return context


class CatalogListView(ListView):
    """
    Gets item list with filtered items
    """
    model = Book
    template_name = 'item_list.html'
    paginate_by = settings.PAGER_TAKE
    search_term = '' # search term for filter

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        # this parameter goes for the right pagination with search query
        context['search_term'] = unicode(self.search_term)

        page = self.request.GET.get('page')
        #Add range template context variable that we can loop through pages
        context['range'] = range(context['paginator'].num_pages)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context['items'] = items
        return context

    def get(self, request, *args, **kwargs):
        self.search_term = request.GET.get('search_term', '').strip()
        return super(CatalogListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_term:
            return Book.objects.filter(name__icontains=self.search_term)
        return Book.objects.all()


class ItemDetailView(DetailView):
    """
    Gets details of an item
    """
    model = Book
    template_name = 'item_details.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['images'] = Book.objects.all().values_list('thumbnail', flat=True)[0:4]
        return context