# -*- coding: utf-8 -*-
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.core.urlresolvers import reverse

from .models import Bet
from .forms import BetForm, ShareForm


class BetListView(ListView):
    """
    """
    model = Bet


class BetCreateView(CreateView):
    """
    """
    model = Bet
    form_class = BetForm
    template_name = 'bet/bet_form.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('bet:detail', kwargs={'slug': self.object.slug})


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
    form_class = BetForm
    template_name = 'bet/bet_form.html'


class CounterBetFormView(BetFormView):
    def get_initial(self):
        initial = super(CounterBetFormView, self).get_initial()
        initial.update({'parent_bet': self.get_object()})
        return initial
