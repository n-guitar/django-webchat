from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from asgiref.sync import sync_to_async

from .models import Channel, Message


class WebChatTop(generic.ListView):
    model = Channel
    template_name = 'webchat/top.html'


class CreateChannel(generic.CreateView):
    template_name = 'webchat/create_channel.html'
    model = Channel
    fields = ('name', 'topic', 'is_private')
    success_url = reverse_lazy('webchat:top')

#  Message.objects.select_related('channel').values('channel__name','channel_id','user__username','user__id','message').get(channel_id=4)


class ChatRoom(LoginRequiredMixin, generic.TemplateView):
    template_name = 'webchat/chat_room.html'

    # オーバーライドしてurl path chat_room/<str:room> を取得
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_id = self.kwargs.get('room_id')
        room_name = Channel.objects.get(id=room_id)
        message_all = Message.objects.select_related('channel').values(
            'channel__name', 'channel_id', 'user__username', 'user__id', 'message').filter(channel_id=room_id)
        context = {
            'room_id': room_id,
            'room_name': room_name,
            'message_all': message_all
        }
        return context


@sync_to_async
def message_save(channel_id, user_id, message):
    """
    read https://docs.djangoproject.com/en/3.1/topics/async/
    非同期でdbへmessageを書き込む
    """
    print(channel_id, user_id, message)
    save_message = Message(channel_id=channel_id,
                           user_id=user_id, message=message)
    save_message.save()


clients = {}


async def websocket_server(socket, room):
    room_path = "/ws/" + room
    await socket.accept()
    key = socket.headers['sec-websocket-key']
    clients[key] = socket
    try:
        while True:
            data = await socket.receive()
            data_list = data['text'].split(',')
            username, user_id, message = data_list[0], data_list[1], data_list[2]
            for client in clients.values():
                if client.path == room_path:
                    print("----------")
                    print(username, user_id, message)
                    await client.send_text("{} => {}".format(username, message))
                    await message_save(channel_id=room, user_id=user_id, message=message)
        await socket.close()
        del clients[key]
