from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class DonationPageView(TemplateView):
    template_name = 'donation.html'