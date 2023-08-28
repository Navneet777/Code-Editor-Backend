from django.urls import path
from authentication.consumers import SomeConsumer

from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.security.websocket import AllowedHostsOriginValidator


websocket_urlpatterns = [
    path('ws/sc/',SomeConsumer.as_asgi())
]