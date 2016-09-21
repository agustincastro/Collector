from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CatalogListView.as_view(), name='index'),
]