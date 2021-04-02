from django.urls import resolve
from .connection import WebSocket, Headers


def websockets(app):
    async def asgi(scope, receive, send):
        # await print_websocket_item(scope, receive, send)
        if scope["type"] == "websocket":
            match = resolve(scope["raw_path"])
            await match.func(WebSocket(scope, receive, send), *match.args, **match.kwargs)
            return
        await app(scope, receive, send)

    return asgi


async def print_websocket_item(scope, receive, send):
    print('-------------scope--------------')
    print('scope[raw_path]: {}'.format(scope['raw_path']))
    print('-------------header--------------')
    header = Headers(scope)
    print('header.keys: {}'.format(header.keys))
    print('header.as_dict: {}'.format(header.as_dict))
