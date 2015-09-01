# -*- coding: utf-8 -*-
import django.dispatch


log_bet_event = django.dispatch.Signal(providing_args=['user', 'instance', 'status'])
