# -*- coding: utf-8 -*-
import django.dispatch


add_bet_log = django.dispatch.Signal(providing_args=['user', 'instance', 'status'])
