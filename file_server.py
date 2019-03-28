import tornado.web


class FileServer(tornado.web.StaticFileHandler):

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.default_filename = 'index.html'

    def data_received(self, chunk):
        pass
