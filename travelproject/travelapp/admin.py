from django.contrib import admin

# Register your models here.
from .models import place,offer

admin.site.register(place)

admin.site.register(offer)