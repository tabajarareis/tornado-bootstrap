import tornado.web
import tornado.httpserver
import tornado.ioloop

from tornado.options import options

from settings import settings
from routes import url_patterns


class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
