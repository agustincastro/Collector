from django.conf.urls import url
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    url(r'^login/$', auth.login, {'template_name': 'authentication/login.html'}, name='login'),
    url(r'^password_reset/$', auth.password_reset, name='password_reset'),
    url(r'^register/$', views.Register.as_view(),  name='register'),

]
