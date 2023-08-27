from django.contrib import admin
from django.urls import path,include
# from authentication.routing import websocket_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
]