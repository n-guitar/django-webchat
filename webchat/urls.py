from django.urls import path
from .views import WebChatTop, chat_room
websocket = path

urlpatterns = [
    path('top/', WebChatTop.as_view(), name='top'),
    path('chat_room/<str:room>', chat_room, name='chat_room'),
]
