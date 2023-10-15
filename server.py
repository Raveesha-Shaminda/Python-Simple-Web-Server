from http.server import HTTPServer , BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def do_get(self):
            if self.path == '/':
                self.path = '/index.html'
                open_file = open(self.path[1.]).read()
                self.send_response(200)
                self.send_error(401)
                self.end_headers()
                self.wfile.write(bytes(open_file, "utf-8"))
          
http = HTTPServer(('localhost',2023), MyServer)
http.serve_forever()
