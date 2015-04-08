from django.contrib import admin
from silver_weather.models import BetterUser, RainFavourite, SunFavourite, SnowFavourite

admin.site.register(BetterUser)
admin.site.register(RainFavourite)
admin.site.register(SunFavourite)
admin.site.register(SnowFavourite)
