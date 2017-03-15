from django.contrib import messages
from django.contrib.auth import views
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.shortcuts import redirect, render
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import View, FormView

from Collector.settings import DEFAULT_FROM_EMAIL
from authentication.forms import UserForm, PasswordResetRequestForm, SetPasswordForm
from authentication.models import User


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
    Handles registration of users
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


class ResetPasswordRequestView(FormView):
    template_name = 'password_reset.html'
    success_url = '/authentication/login'
    form_class = PasswordResetRequestForm

    @staticmethod
    def validate_email_address(email):
        '''
        Static function for email validation
        '''
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def get(self, request, *args, **kwargs):
        form = PasswordResetRequestForm()
        return render(request, 'authentication/password_reset.html', {'form': form})

    def post(self, request, *args, **kwargs):
        '''
        A normal post request which takes input from field "email" (in ResetPasswordRequestForm).
        '''
        form = self.form_class(request.POST)
        form_email = ''
        if form.is_valid():
            form_email = form.cleaned_data["email"]
        if self.validate_email_address(form_email):  # uses the method written above
            '''
            Verifies that the submited email is valid and gets its asociated user. If it is registered an
            email will be sent to that address with the reset link
            '''
            try:
                user = User.objects.get(email=form_email)
            except User.DoesNotExist:
                user = None

            if user is not None:
                email_template_data = {
                    'email': user.email,
                    'domain': request.META['HTTP_HOST'],
                    'site_name': 'Collector',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                email_template_name = 'authentication/password_reset_email.html'
                subject = 'Password reset on Collector'
                email = loader.render_to_string(email_template_name, email_template_data)

                send_mail(subject, email, DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
                result = self.form_valid(form)
                messages.success(request,
                             'An email has been sent to ' + form_email + ". Please check its inbox to continue reseting password.")
                return result
            else:
                result = self.form_invalid(form)
                messages.error(request, 'No user is associated with this email address')
                return result

        messages.error(request, 'Invalid Input')
        return self.form_invalid(form)


class PasswordResetConfirmView(FormView):
    """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
    """
    template_name = 'authentication/password_reset_enter_new.html'
    success_url = '/authentication/login'
    form_class = SetPasswordForm

    def get(self, request, uidb64=None, token=None, *arg, **kwargs):
        form = SetPasswordForm()
        return render(request, "authentication/password_reset_enter_new.html", {'form': form})

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):

        UserModel = User
        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password = form.cleaned_data['new_password']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been reset.')
                return self.form_valid(form)
            else:
                messages.error(request, 'Password reset has not been unsuccessful.')
                return self.form_invalid(form)
        else:
            messages.error(request, 'The reset password link is no longer valid.')
            return self.form_invalid(form)

