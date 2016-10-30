from django.conf.urls import url
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', auth.logout_then_login, name='logout'),
    url(r'^register/$', views.Register.as_view(),  name='register'),
    url(r'^reset_password/$', views.ResetPasswordRequestView.as_view(), name="password_reset"),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.PasswordResetConfirmView.as_view(), name='reset_password_confirm'),

]
