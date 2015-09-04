# -*- coding: utf-8 -*-
from kamraapp.utils import get_namedtuple_choices

default_app_config = 'kamraapp.apps.bet.apps.BetConfig'

SUB_BET_TYPE = get_namedtuple_choices('SUB_BET_TYPE', (
    ('parent', 'parent', 'Parent'),
    ('clone', 'clone', 'Clone'),
    ('bet_for', 'bet_for', 'For'),
    ('bet_against', 'bet_against', 'Against'),
))
