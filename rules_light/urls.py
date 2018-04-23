from __future__ import unicode_literals

from django.urls import path

from .views import RegistryView


urlpatterns = [
    path('', RegistryView.as_view(), name='rules_light_registry'),
]
