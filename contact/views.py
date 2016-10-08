from django.views.generic import View
from django.shortcuts import render_to_response, render
from .forms import ContactForm
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.conf import settings


class ContactView(View):
    """
    View that handles the contact form
    GET: Displays the contact form
    POST: If the data is OK, it sends and email and displays a correct message.
          If not, it displays the corresponding fields with errors
    """

    def get(self, request):
        return render(request, 'contact.html', {'contact_form': ContactForm()})

    def post(self, request):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            sender = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            mail = EmailMessage('Book Collector contact message',
                                name + ' (email: ' + sender + ') send us this message: \n\n' + message,
                                sender,
                                [settings.EMAIL_RECEIVER], headers={'Reply-To': sender})
            mail.send()
            return render(request, 'contact.html',
                          {'contact_form': contact_form,
                           'result_message': 'Message was sent! We will answer as soon as posible.'})
        else:
            return render(request, 'contact.html', {'contact_form': contact_form})
