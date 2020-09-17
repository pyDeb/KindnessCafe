from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from Accounts.models import User
from KindnessCafe import settings
import urllib.request
from json import loads
from datetime import datetime
from django.core.mail import EmailMessage
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm


# Create your views here.


def donation_view(request):
    if request.method == 'POST':
        errors = {}

        ### validating user's input
        if len(request.POST['phone']) < 10:
            errors['phone'] = "You must enter a valid phone number"
        
        if len(request.POST['address']) < 10:
            errors['address'] = "You must enter a address"


        if(len(str(request.POST['pickuptime'])) == 0):
            errors['pickuptime'] = "You must enter the time to pickup"

        else:
            time_now = str(datetime.now()).split(' ')[1].split('.')[0]
            hour_now = time_now.split(':')[0]
            if hour_now < request.POST['pickuptime']:
                errors['pickuptime'] = "It seems that pickup time is invalid"

        if(len(str(request.POST['date'])) == 0):
            errors['date'] = "You must enter the date of pickup"

        else:
            date_now = str(datetime.now()).split(' ')[0]
            year_now = date_now.split('-')[0]
            month_now = date_now.split('-')[1]
            day_now = date_now.split('-')[2]


            if ((request.POST['date'].split('/')[2] < year_now) or (request.POST['date'].split('/')[2] == year_now and request.POST['date'].split('/')[0] < month_now) \
            or (request.POST['date'].split('/')[2] == year_now and request.POST['date'].split('/')[0] == month_now and request.POST['date'].split('/')[1]) < day_now): 
                errors['date'] = "The date is invalid"

        if (len(str(request.POST['itemlist'])) == 0):
            errors['itemlist'] = "Please fill out the items you would like to donate"
        


        
        if len(errors):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            return redirect('/donation')

        """ Begin reCAPTCHA validation """
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = loads(response.read().decode())
        """ End reCAPTCHA validation """

        if result['success']:
            mail_subject = 'DONATION'
            message =  mail_subject  + '\n' + "Pickup Date: " + request.POST['date'] + '\n' + \
                'pickup time' + request.POST['pickuptime'] + '\n' + 'Phone Number: ' + request.POST['phone'] + '\n' + 'Address: ' + request.POST['address'] + \
                    '\n' + 'List of Items: '  + request.POST['itemlist']
            to_email = settings.EMAIL_HOST_USER + '@gmail.com'
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
                )
            email.send()
        

            return redirect("/", messages.success(request, 'Your message was sent. We will contact you soon!'))
        else:
            return redirect('/donation', messages.error(request, 'Please solve the reCAPTCHA again.'))

    else:
        first_name = ""
        if request.session.has_key('id'):
            first_name = User.objects.filter(id=request.session['id'])[0].first_name
        return render(request, 'donation.html', {'first_name' : first_name})



    

def process_payment(request):
    if request.method == 'POST':
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': '%.2f' % request.POST[''](
                Decimal('.01')),
            'item_name': 'DONATION TO KINDNESS CAFE WINDSOR',
            'currency_code': 'CAD',
            'notify_url': 'http://{}{}'.format(host,
                                            reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                            reverse('payment_done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                reverse('payment_cancelled')),
        }

        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'process_payment.html')

    #else:





def payment_done(request):
    return render(request, 'payment_done.html')


def payment_cancelled(request):
    return render(request, 'payment_cancelled.html')





