from django.urls import path
from .views import WebChatTop
websocket = path

urlpatterns = [
    path('top/', WebChatTop.as_view(), name='top')
]
