from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf.urls.static import static

from Collector import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', lambda r: HttpResponseRedirect('catalog/')),
    url(r'^catalog/', include('catalog.urls')),

]

# Path to media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)