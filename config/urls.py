from django.contrib import admin
from django.urls import path, include
from webchat.urls import websocket
from webchat import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ws/<str:room>', views.websocket_server),
    path('webchat/', include('webchat.urls')),
]
