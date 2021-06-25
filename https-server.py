import ssl
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8888
ADDRESS = "0.0.0.0"


class LauncherService(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            f = open(sys.argv[1], 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            return
        except IOError:
            self.send_error(404, 'file not found')


try:
    httpd = HTTPServer((ADDRESS, PORT), LauncherService)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   keyfile="localhost.pem",
                                   certfile="localhost.pem",
                                   server_side=True,
                                   ssl_version=ssl.PROTOCOL_TLS)
    print(f'https server is running at https://{httpd.server_address[0]}:{httpd.server_port}')
    httpd.serve_forever()
except:
    httpd.shutdown()


