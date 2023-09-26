from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # определяем метод `do_GET` 
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


httpd = HTTPServer(('172.30.4.248', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
