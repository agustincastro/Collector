from django.contrib.auth import views
from django.shortcuts import redirect, render
from django.views.generic import View

from authentication.forms import UserForm


def Login(request):
    """
    Adds signup form as an extra context variable
    """
    signup_form = UserForm()
    template_response = views.login(request, template_name='authentication/login.html',
                                    extra_context={'signup_form': signup_form})
    return template_response



class Register(View):
    """
    Handles resgistration of users
    """

    def post(self, request):
        return redirect('Index')

    def get(self, request):
        form = UserForm()
        return render(request, 'authentication/register.html', {'form': form})
