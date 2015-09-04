# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.generic import UpdateView, ListView, DetailView

from formtools.wizard.views import SessionWizardView

from .models import Bet
from .forms import BetFormStep1, BetFormStep2, ShareForm


class BetListView(ListView):
    """
    """
    model = Bet


class BetCreateView(SessionWizardView):
    """
    """
    TEMPLATES = {
        '0': 'bet/bet_form_with_donation_recipients.html'
    }
    form_list = [BetFormStep1, BetFormStep2]
    template_name = 'bet/bet_form.html'

    def get_template_names(self):
        try:
            return [self.TEMPLATES[self.steps.current]]
        except:
            return self.template_name

    def done(self, form_list, form_dict, **kwargs):
        bet, is_new = form_dict['0'].save()
        user, is_new = form_dict['1'].save()

        # save the user associated with this bet
        bet.user = user
        bet.save(update_fields=['user'])

        return redirect(reverse('bet:detail', kwargs={'slug': bet.slug}))


class BetDetailView(DetailView):
    """
    """
    model = Bet

    def get_context_data(self, *args, **kwargs):
        context = super(BetDetailView, self).get_context_data(*args, **kwargs)
        url = self.request.build_absolute_uri()
        context.update({
            'facebook_share_form': ShareForm(initial={'text': 'facebook share content here: %s' % url}),
            'twitter_share_form': ShareForm(initial={'text': 'twitter share content here: %s' % url}),
        })
        return context


class BetFormView(UpdateView):
    """
    """
    model = Bet
    form_class = BetFormStep1
    template_name = 'bet/bet_form.html'


class CounterBetFormView(BetFormView):
    def get_initial(self):
        initial = super(CounterBetFormView, self).get_initial()
        initial.update({'parent_bet': self.get_object()})
        return initial
