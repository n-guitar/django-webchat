from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Channel


class WebChatTop(generic.ListView):
    model = Channel
    template_name = 'webchat/top.html'


class CreateChannel(generic.CreateView):
    template_name = 'webchat/create_channel.html'
    model = Channel
    fields = ('name', 'topic', 'is_private')
    success_url = reverse_lazy('webchat:top')


class ChatRoom(LoginRequiredMixin, generic.TemplateView):
    template_name = 'webchat/chat_room.html'

    # オーバーライドしてurl path chat_room/<str:room> を取得
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_id = self.kwargs.get('room_id')
        room_name = Channel.objects.get(id=room_id)
        context = {
            'room_id': room_id,
            'room_name': room_name
        }
        return context


# def chat_room(request, room):
#     object = room
#     return render(request, 'webchat/chat_room.html', {'object': object})


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
            print("user: {}, message: {}".format(data_list[0], data_list[1]))
            for client in clients.values():
                if client.path == room_path:
                    await client.send_text("{} => {}".format(data_list[0], data_list[1]))
    except:
        await socket.close()
        del clients[key]
