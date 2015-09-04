# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models import DonationRecipient


class DonationRecipientSerializer(serializers.ListSerializer):
    class Meta:
        model = DonationRecipient
