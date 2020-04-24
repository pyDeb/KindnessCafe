from django.shortcuts import render
from Accounts.models import User
# Create your views here.


def donation_view(request):
    first_name = ""
    if request.session.has_key('id'):
        first_name = User.objects.filter(id=request.session['id'])[0].first_name
    return render(request, 'donation.html', {'first_name' : first_name})