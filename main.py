import asyncio

import tornado.ioloop
import tornado.web
from tornado.platform.asyncio import AnyThreadEventLoopPolicy

from file_server import FileServer
from websocket_server import WebSocket

if __name__ == "__main__":
    asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())

    server = tornado.web.Application([
        (r"/socket", WebSocket, {'named_arguement': 'example'}),
        (r"/(.*)", FileServer, {"path": "./files"})])

    server.listen(8000)

    # Start IOLoop
    tornado.ioloop.IOLoop.current().start()
