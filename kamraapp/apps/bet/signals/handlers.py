# -*- coding: utf-8 -*-
from django.dispatch import receiver
from pinax.eventlog.models import log

from . import add_bet_log

import datetime


@receiver(add_bet_log, dispatch_uid='bet._log_bet_event')
def _log_bet_event(user, instance, status, *args, **kwargs):
    """
    Log a custom event
    """
    log(user=user,
        action=status.lower(),
        obj=instance,
        dateof=datetime.datetime.utcnow(),
        extra=kwargs)
