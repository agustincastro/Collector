from django.conf.urls import url
from .views import ContactView


urlpatterns = [
    url(r'^$', view=ContactView.as_view(), name='contact'),
]