from django.apps import AppConfig


class DonationAppConfig(AppConfig):
    name = 'Donation'

    def ready(self):
        # import signal handlers
        from . import signal
