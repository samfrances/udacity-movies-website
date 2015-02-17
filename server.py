from wsgiref.simple_server import make_server

class App():
    def __init__(self, html):
        self.html = html

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [self.html]

class VerySimpleServer():
    def __init__(self, html):
        self.app = App(html)

    def run(self):
        srv = make_server('localhost', 8080, self.app)
        print("Serving at http://localhost:8080/")
        srv.serve_forever()

if __name__ == "__main__":
    VerySimpleServer("Hello beautiful world!!").run()
