from django.contrib.auth import views
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def Login(request):
    template_response = views.login(request)
    # return redirect('Index')


class Register(View):
    """
    Handles resgistration of users
    """

    def post(self, request):
        return redirect('Index')

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'authentication/register.html', {'form': form})
