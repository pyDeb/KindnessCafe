from django.urls import path
from .views import donation_view

urlpatterns = [
    path('donation/', donation_view, name='donation'), 
]