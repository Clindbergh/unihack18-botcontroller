
import json
import uuid

import tornado.websocket


class WebSocket(tornado.websocket.WebSocketHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.id = uuid.uuid4()

    def __eq__(self, other):
        return self.id == other.id

    def initialize(self, **kwargs):
        print(kwargs['named_arguement'])
        pass

    def data_received(self, chunk):
        pass

    def check_origin(self, origin):
        return True

    def open(self):
        print("connected")

    def on_message(self, message):
        data = self.try_parse_json(message)
        if data:
            print(str(self.id) + "\n" + message)

    def on_close(self):
        print("disconnected")

    def send_message(self, message):
        if not isinstance(message, str):
            message = json.dumps(message)

        self.write_message(message)

    def try_parse_json(self, msg):
        try:
            return json.loads(msg)
        except TypeError:
            return json.loads(msg.decode())
        except ValueError:
            print("Bad JSON:")
            print(msg)
            self.write_message({'t': 'e', 'd': {'error': 'bad_json_format', 'msg': msg}})
            return False
