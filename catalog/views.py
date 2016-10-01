from django.shortcuts import render
from django.views.generic import ListView
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