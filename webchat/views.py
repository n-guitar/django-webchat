from django.shortcuts import render
from django.views import generic


class WebChatTop(generic.TemplateView):
    template_name = 'webchat/top.html'


async def websocket_view(socket):
    await socket.accept()
    await socket.send_text('hello')
    await socket.close()
