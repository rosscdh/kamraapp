from django.contrib import admin

from .models import Bet, DonationRecipient, Proof


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    search_fields = ['slug', 'name', 'description', 'recipients__name']
    list_display = ('name', 'description', 'sub_bet_type',)
    list_filter = ('sub_bet_type',)


@admin.register(DonationRecipient)
class DonationRecipientAdmin(admin.ModelAdmin):
    search_fields = ['slug', 'name', 'url', 'id']
    list_display = ('name', 'url', 'weight',)


admin.site.register([Proof])
