from django.contrib import admin
from .models import Instrument, Played, Accessory

# Register your models here.

admin.site.register(Instrument)
admin.site.register(Played)
admin.site.register(Accessory)