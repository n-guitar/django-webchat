from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User


class WebChatTop(generic.TemplateView):
    template_name = 'webchat/top.html'


class ChatRoom(LoginRequiredMixin, generic.TemplateView):
    template_name = 'webchat/chat_room.html'

    # オーバーライドしてurl path chat_room/<str:room> を取得
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.kwargs.get('room')
        context = {'object': object}
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
