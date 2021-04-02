from django.urls import path
from .views import WebChatTop, ChatRoom, CreateChannel


websocket = path
app_name = 'webchat'
urlpatterns = [
    path('top/', WebChatTop.as_view(), name='top'),
    path('create_channel', CreateChannel.as_view(), name='create_channel'),
    path('chat_room/<str:room_id>', ChatRoom.as_view(), name='chat_room'),
]
