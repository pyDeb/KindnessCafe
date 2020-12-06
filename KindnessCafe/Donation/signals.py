from django.shortcuts import get_object_or_404
from .models import Donation
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        donation = get_object_or_404(Donation, id=ipn.invoice)

        if donation.amount == ipn.mc_gross:
            # mark the order as paid
            donation.paid = True
            order.save()