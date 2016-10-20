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
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('index')

        else:
            template_response = views.login(request, template_name='authentication/login.html',
                                    extra_context={'signup_form': user_form})
            return template_response


    #def get(self, request):
    #    form = UserForm()
    #    return render(request, 'authentication/register.html', {'form': form})
