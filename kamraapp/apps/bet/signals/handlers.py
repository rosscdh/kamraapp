# -*- coding: utf-8 -*-
from pinax.eventlog.models import log

import datetime


def _log_bet_event(user, instance, status, *args, **kwargs):
    """
    Log a custom event
    """
    log(user=user,
        action=status.lower(),
        obj=instance,
        dateof=datetime.datetime.utcnow(),
        extra=kwargs)
