# -*- coding: utf-8 -*-
from django.db import models

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status as http_status
from rest_framework.decorators import detail_route
#from rest_framework_extensions.mixins import CacheResponseAndETAGMixin

from ..models import Bet, DonationRecipient
from .serializers import BetSerializer, DonationRecipientSerializer


class BetViewset(viewsets.ReadOnlyModelViewSet):
    """
    """
    model = Bet
    serializer_class = BetSerializer
    queryset = Bet.objects.all()

    @detail_route(methods=['GET', 'POST'])
    def bets_for(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            data = self.object.data.get('bets_for', self.object.updated_bets_data(bet_type=self.object.SUB_BET_TYPE.bet_for))
        else:
            # do posty stuff
            new_bet = self.get_object()
            new_bet.pk = None
            new_bet.slug = None
            new_bet.user = request.user
            new_bet.parent_bet = self.object
            new_bet.sub_bet_type = new_bet.SUB_BET_TYPE.bet_for
            new_bet.data = {}
            new_bet.save()
            # update the original bet data
            self.object.data['bets_for'] = data = self.object.updated_bets_data(bet_type=self.object.SUB_BET_TYPE.bet_for)
            self.object.save(update_fields=['data'])

        return Response(data, status=http_status.HTTP_200_OK)

    @detail_route(methods=['GET', 'POST'])
    def bets_against(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            data = self.object.data.get('bets_against', self.object.updated_bets_data(bet_type=self.object.SUB_BET_TYPE.bet_against))
        else:
            # do posty stuff
            new_bet = self.get_object()
            new_bet.pk = None
            new_bet.slug = None
            new_bet.user = request.user
            new_bet.parent_bet = self.object
            new_bet.sub_bet_type = new_bet.SUB_BET_TYPE.bet_against
            new_bet.data = {}
            new_bet.save()
            self.object.data['bets_against'] = data = self.object.updated_bets_data(bet_type=self.object.SUB_BET_TYPE.bet_against)
            # update the data
            self.object.save(update_fields=['data'])

        return Response(data, status=http_status.HTTP_200_OK)


class DonationRecipientViewset(viewsets.ReadOnlyModelViewSet):
    """
    """
    model = DonationRecipient
    serializer_class = DonationRecipientSerializer
    queryset = DonationRecipient.objects.all()
