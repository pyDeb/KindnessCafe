from django.urls import path
from .views import donation_view, payment_done, payment_cancelled, process_payment

urlpatterns = [
    path('donation/', donation_view, name='donation'), 
    path('process-payment/', process_payment, name='process_payment'),
    path('payment-done/', payment_done, name='payment_done'),
    path('payment-cancelled/', payment_cancelled, name='payment_cancelled'),

]