from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from Accounts.models import User
from KindnessCafe import settings
import urllib.request
from json import loads
from datetime import datetime
from django.core.mail import EmailMessage
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import Donation

# Create your views here.


def donation_view(request):
    if request.method == 'POST':

        # """ Begin reCAPTCHA validation """
        # recaptcha_response = request.POST.get('g-recaptcha-response')
        # url = 'https://www.google.com/recaptcha/api/siteverify'
        # values = {
        #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        #     'response': recaptcha_response
        # }
        # data = urllib.parse.urlencode(values).encode()
        # req =  urllib.request.Request(url, data=data)
        # response = urllib.request.urlopen(req)
        # result = loads(response.read().decode())
        # """ End reCAPTCHA validation """
        # if result['success']:
        
        ### ITEM DONATION BEGIN
        if 'item-donation' in request.POST:
        ### validating user's input
            # print(request.POST.getlist('inputFoodItems'))
            mail_subject = 'DONATION'
            item_list = ", ".join(request.POST.getlist('inputFoodItems'))
            
            message =  mail_subject  + '\n' + "Phone Number: " + request.POST['inputPhone'] + '\n' + \
                'Email Address: ' + request.POST['inputEmail'] + '\n' + 'Address: ' + request.POST['inputAddress'] + '\n' + \
                'Items: ' + item_list
            to_email = settings.EMAIL_HOST_USER + '@gmail.com'
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
                )
            email.send()
        

            return redirect("/", messages.success(request, 'Your message was sent. We will contact you soon!'))
        
        elif 'PayPal_donation' in request.POST:
                host = request.get_host()
                name = request.POST['inputName']
                if name:
                    name = "Anonymous"

                don = Donation(name=name, amount=float(request.POST['amount']))
                don.save()
                
                paypal_dict = {
                    'business': settings.PAYPAL_RECEIVER_EMAIL,
                    'amount': request.POST['inputAmount'],
                    'item_name': 'Donation for Kindness Cafe',
                    'invoice': str(don.d_id),
                    'currency_code': 'CAD',
                    'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
                    'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
                    'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
                }

                form = PayPalPaymentsForm(initial=paypal_dict)
                return render(request, 'process_payment.html', {'form': form})


        # else:
        #     return redirect('/donation', messages.error(request, 'Please solve the reCAPTCHA again.'))

    else:
        first_name = ""
        if request.session.has_key('id'):
            first_name = User.objects.filter(id=request.session['id'])[0].first_name
        return render(request, 'donation.html', {'first_name' : first_name})





@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled.html')
