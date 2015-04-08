from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from tastypie.api import Api
from silver_weather.api.resources import RainFavouriteResource, SunFavouriteResource, SnowFavouriteResource
from golden_weather import settings

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(RainFavouriteResource())
v1_api.register(SunFavouriteResource())
v1_api.register(SnowFavouriteResource())

urlpatterns = patterns('',
    url(r'^register/$', 'silver_weather.views.register', name='register'),
    url(r'^profile/$', 'silver_weather.views.profile', name='profile'),
    url(r'^$', 'silver_weather.views.home', name='home'),
    url(r'^favourites/$', 'silver_weather.views.favourites', name='favourites'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^api/', include(v1_api.urls)),



    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
