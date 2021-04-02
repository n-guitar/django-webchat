from .connection import WebSocket


def websockets(app):
    async def asgi(scope, receive, send):
        await print_websocket_item(scope, receive, send)
        if scope['type'] == 'http':
            await app(scope, receive, send)
        elif scope["type"] == "websocket":
            await WebSocket(scope, receive, send)
    return asgi


async def print_websocket_item(scope, receive, send):
    print('-------------scope--------------')
    print('scope: {}'.format(scope))
    print('-------------receive--------------')
    print('receive: {}'.format(receive))
    print('-------------send--------------')
    print('send: {}'.format(send))
