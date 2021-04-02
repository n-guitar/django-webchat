from django.urls import path
from .views import WebChatTop, ChatRoom


websocket = path
app_name = 'webchat'
urlpatterns = [
    path('top/', WebChatTop.as_view(), name='top'),
    # path('chat_room/<str:room>', chat_room, name='chat_room'),
    path('chat_room/<str:room>', ChatRoom.as_view(), name='chat_room'),
]
