import os
import sys
import inspect
currentpath = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentpath = os.path.dirname(currentpath)
sys.path.insert(0, parentpath)

import tornado.testing
from application import Application


class ApplicationTest(tornado.testing.AsyncHTTPTestCase):

    def get_app(self):
        return Application()

    def test_index(self):
        self.http_client.fetch(self.get_url('/'), self.stop)
        response = self.wait()
        self.assertEqual(200, response.code)
