# myapp/apps.py
from django.apps import AppConfig
#from django.dispatch import receiver
from kamraapp.apps.bet.signals.handlers import _log_bet_event


class BetConfig(AppConfig):
    name = 'kamraapp.apps.bet'

    def ready(self): pass
