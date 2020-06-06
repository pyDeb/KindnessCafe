from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from Accounts.models import User
from KindnessCafe import settings
import urllib
from json import loads
# Create your views here.


def donation_view(request):
    if request.method == 'POST':
        errors = {}
        ### validating user's input
        if len(request.POST['email']) == 0:
            errors['email'] = "You must enter an email"
        

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
            return redirect("/", messages.success(request, 'Your message was sent. We will contact you soon!'))
        else:
            return redirect('/donation', messages.error(request, 'Please try again'))

    else:
        first_name = ""
        if request.session.has_key('id'):
            first_name = User.objects.filter(id=request.session['id'])[0].first_name
        return render(request, 'donation.html', {'first_name' : first_name})