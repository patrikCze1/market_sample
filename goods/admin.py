from django.contrib import admin

from .models import Offer, Comment, Image

@admin.register(Offer, Comment, Image)
class OfferAdmin(admin.ModelAdmin):
    pass