# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from authentication.routing import websocket_urlpatterns  # Replace with your app's routing module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_editor_backend.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
            websocket_urlpatterns
        )
})
