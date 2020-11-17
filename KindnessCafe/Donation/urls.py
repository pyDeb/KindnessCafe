from django.urls import path, include
from . import views


urlpatterns = [
    path('donation/', views.donation_view, name='donation'), 
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('paypal/', include('paypal.standard.ipn.urls')),


]