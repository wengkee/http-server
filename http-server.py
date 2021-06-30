import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8888
ADDRESS = ""


class LauncherService(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            with open(sys.argv[1], 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f.read())
            return
        except IOError:
            self.send_error(404, 'file not found')


try:
    httpd = HTTPServer((ADDRESS, PORT), LauncherService)
    print(f'http server is running at http://{httpd.server_address[0]}:{httpd.server_port}')
    httpd.serve_forever()
except:
    httpd.shutdown()


