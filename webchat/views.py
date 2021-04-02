from django.shortcuts import render, redirect
from django.views import generic


class WebChatTop(generic.TemplateView):
    template_name = 'webchat/top.html'


def chat_room(request, room):
    # if request.method == 'POST':
    #     title = request.POST['title']
    #     memo = request.POST['memo']
    #     Todo.objects.filter(pk=pk).update(title=title, memo=memo)
    #     return redirect('list')
    # object = Todo.objects.get(pk=pk)
    object = room
    return render(request, 'webchat/chat_room.html', {'object': object})


clients = {}


async def websocket_view(socket, room):
    print(room)
    await socket.accept()
    # key = socket.headers.as_dict['sec-websocket-key']
    # clients[key] = socket
    try:
        while True:
            data = await socket.receive()
            await socket.send_text(data['text'])
            # for client in clients.values():
            #     await client.send_text("ID: {} => {}".format(key, data['text']))
    except:
        await socket.close()
        # del clients[key]
