"""Provides a very simple WSGI server, which simply serves html
provided as a string to http://localhost:8080/"""

from wsgiref.simple_server import make_server

class App(object):
    def __init__(self, html):
        self.html = html

    def __call__(self, environ, start_response):
        """Makes App objects callable, like functions, as required by WSGI"""
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [self.html]

class VerySimpleServer(object):
    def __init__(self, html):
        self.app = App(html)

    def run(self):
        srv = make_server('localhost', 8080, self.app)
        print("Serving at http://localhost:8080/")
        srv.serve_forever()

if __name__ == "__main__":
    VerySimpleServer("Hello beautiful world!!").run()
