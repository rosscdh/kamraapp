# -*- coding: utf-8 -*-
# from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand

from termcolor import colored

from kamraapp.apps.bet.models import DonationRecipient
# from pyquery import PyQuery as pq
import urllib

import requests


class Command(BaseCommand):
    """
    Generate the tab separated csv files from amazon page
    """
    uri = 'https://api.betterplace.org/de/api_v4/projects.json'

    def add_arguments(self, parser):
        parser.add_argument('--country', action='store_true', dest='country', default='Deutschland', help='Specify alternate country')
        parser.add_argument('--start_page', action='store_true', dest='start_page', default=1, help='Which Page to start at')
        parser.add_argument('--num_pages', action='store_true', dest='num_pages', default=2, help='Number of pages to retrieve')
        parser.add_argument('--add_all', action='store_true', dest='add_all', default=False, help='Just add all items without prompts')

    def handle(self, *args, **options):
        for page in range(0, options.get('num_pages')):
            params = {
                'page': options.get('start_page') + page,
                'per_page': 25,
                'country': options.get('country')
            }
            query_pairs = [(key, value) for key, value in params.iteritems()]
            query_string = urllib.urlencode(query_pairs)
            uri = '%s?%s' % (self.uri, query_string)

            resp = requests.get(uri)
            for item in resp.json().get('data', []):
                name = item.pop('title', None)
                description = item.pop('description', None)
                slug = slugify(name)

                try:
                    url = None
                    for u in item.get('links', []):
                        if u.get('rel') == 'platform':
                            url = u.get('href')
                            break
                except:
                    url = None

                weight = 0
                if options.get('add_all') is False:
                    try:
                        DonationRecipient.objects.get(slug=slug)
                        exists = True
                    except DonationRecipient.DoesNotExist:
                        exists = False

                    message = '(exists: %s) %s - %s' % (exists, name, url)
                    print(colored(message, 'green' if exists is False else 'magenta', attrs=['reverse', 'blink']))
                    weight = raw_input(colored('Article weight? (0 default, "n" wont import):', 'yellow', attrs=['reverse', 'blink']))
                    # handle no events
                    if weight == 'n':
                        continue

                recipient, is_new = DonationRecipient.objects.get_or_create(slug=slug)
                recipient.name = name
                recipient.description = description
                recipient.url = url
                item.update({
                    'meta': {
                        'provider': 'betterplace'
                    }
                })
                recipient.weight = weight
                recipient.data = item
                recipient.save()
