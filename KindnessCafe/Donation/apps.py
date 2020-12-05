from django.apps import AppConfig


class DonationConfig(AppConfig):
    name = 'Donation'

    def ready(self):
        # import signal handlers
        import Donation.signals
