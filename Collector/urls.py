from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', lambda r: HttpResponseRedirect('catalog/')),
    url(r'^catalog/', include('catalog.urls')),

]
