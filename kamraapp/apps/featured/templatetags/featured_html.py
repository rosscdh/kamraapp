# -*- coding: utf-8 -*-
from django import template

from ..models import FeaturedDonationRecipient

register = template.Library()


@register.inclusion_tag('featured/partial/featured_recipients.html')
def featured_recipients():
    return {
        'objects_list': FeaturedDonationRecipient.objects.all()[:5]
    }

