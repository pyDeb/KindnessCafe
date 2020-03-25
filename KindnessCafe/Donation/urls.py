from django.urls import path
from .views import DonationPageView

urlpatterns = [
    path('donation/', DonationPageView.as_view(), name='donation'), 
]