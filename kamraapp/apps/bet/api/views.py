# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework_extensions.mixins import CacheResponseAndETAGMixin

from ..models import DonationRecipient
from .serializers import DonationRecipientSerializer


# class DonationRecipientViewset(CacheResponseAndETAGMixin,
#                                viewsets.ReadOnlyModelViewSet):
class DonationRecipientViewset(viewsets.ReadOnlyModelViewSet):
    """
    """
    model = DonationRecipient
    serializer_class = DonationRecipientSerializer
    queryset = DonationRecipient.objects.all()
