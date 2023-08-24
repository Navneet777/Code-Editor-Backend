from django.contrib import admin
from django.urls import path,include
from . routing import websocket_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
] + websocket_urlpatterns