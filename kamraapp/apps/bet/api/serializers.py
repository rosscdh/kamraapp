# -*- coding: utf-8 -*-
from django.utils.encoding import smart_text
from django.contrib.auth import get_user_model
from django.template.defaultfilters import truncatewords_html

from rest_framework import serializers

from ..models import Bet, DonationRecipient


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('pk', 'first_name')


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        exclude = ('access_secret', 'access_token', 'data')


class DonationRecipientSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = DonationRecipient
        exclude = ('data',)

    def get_tags(self, obj):
        return obj.tag.split(',') if obj.tag else []

    def get_provider_links(self, obj):
        links = {}
        for link in self.data.get('links', []):
            links[link.get('rel')] = link.get('href')
        return links

    def get_picture(self, obj):
        default_url = 'https://placeholdit.imgix.net/~text?txtsize=33&txt=%s&w=350&h=175' % obj.name
        try:
            for i in obj.data.get('profile_picture', {}).get('links', []):
                if i.get('rel') == 'fill_270x141':
                    return i.get('href')
        except:
            pass
        return default_url

    def get_location(self, obj):
        latitude = obj.data.get('latitude')
        longitude = obj.data.get('longitude')
        street = smart_text(obj.data.get('street'))
        zip_code = smart_text(obj.data.get('zip'))
        city = smart_text(obj.data.get('city'))
        country = smart_text(obj.data.get('country'))
        return {
            # 'general': u'{street}, {zip}, {city}, {country}'.format(street=street,
            #                                                        zip=zip_code,
            #                                                        city=city,
            #                                                        country=country),
            'latitude': latitude,
            'longitude': longitude,
            'street': street,
            'zip': zip_code,
            'city': city,
            'country': country,
        }

    def get_short_description(self, obj):
        return truncatewords_html(obj.description, 15)

    def get_url(self, obj):
        return obj.get_absolute_url()



