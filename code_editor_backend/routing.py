# myproject/routing.py
from django.urls import path
from authentication.consumers import SocketConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("socket.io/", SocketConsumer.as_asgi()),
        ])
    ),
})
