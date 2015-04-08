from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from silver_weather.api.authorization import UserObjectsOnlyAuthorization
from silver_weather.models import *


class RainFavouriteResource(ModelResource):
    class Meta:
        queryset = RainFavourite.objects.all()
        resource_name = "rainfavourite"
        allowed_methods = ['get', 'post', 'put', 'delete']
        # authorization = DjangoAuthorization()
        authentication = SessionAuthentication()
        authorization = UserObjectsOnlyAuthorization()


class SunFavouriteResource(ModelResource):
    class Meta:
        queryset = SunFavourite.objects.all()
        resource_name = "sunfavourite"
        allowed_methods = ['get', 'post', 'put', 'delete']
        # authorization = DjangoAuthorization()
        authentication = SessionAuthentication()
        authorization = UserObjectsOnlyAuthorization()


class SnowFavouriteResource(ModelResource):
    class Meta:
        queryset = SnowFavourite.objects.all()
        resource_name = "snowfavourite"
        allowed_methods = ['get', 'post', 'put', 'delete']
        # authorization = DjangoAuthorization()
        authentication = SessionAuthentication()
        authorization = UserObjectsOnlyAuthorization()
