# -*- coding: utf-8 -*-
from django import forms

#from crispy_forms.helper import FormHelper

from .models import Bet


class BetForm(forms.ModelForm):
    name = forms.CharField(label='I swear that I will:')
    description = forms.CharField(label='A more detailed examination of the commitment:', widget=forms.Textarea)

    class Meta:
        model = Bet
        exclude = ('slug', 'uuid', 'parent_bet_id', 'created_at', 'updated_at')

    # @property
    # def helper(self):
    #     helper = FormHelper()
    #     helper.form_id = 'support-form'
    #     helper.form_class = 'form'
    #     helper.form_method = 'POST'
    #     return helper


class ShareForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class CanModifyForm(forms.Form):
    password = forms.CharField()

    def __init__(self, bet, *args, **kwargs):
        self.bet = bet
        super(CanModifyForm, self).__init__(*args, **kwargs)

    def validate_password(self, value):
        if self.bet.slug != value:
            forms.ValidationError('Incorrect Password Please try again')
        return value
