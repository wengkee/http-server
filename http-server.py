import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer


def parsing_args():
    parser = argparse.ArgumentParser(description="Host a HTTP/HTTPS server")
    parser.add_argument("filename", metavar="filename", type=str,
                        help="the filename of the data file to be hosted by the server")
    parser.add_argument("-p, --port", type=int, default=8080, dest="port",
                        help="the port of the server")
    parser.add_argument("-a, --address", type=str, default="127.0.0.1", dest="address",
                        help="the address of the server")
    return parser.parse_args()


def check_file(file):
    try:
        with open(file, 'rb') as f:
            return f.read()
    except IOError:
        return None


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(content)


args = parsing_args()
filename = args.filename
address = args.address
port = args.port
content = check_file(filename)

if content:

    httpd = HTTPServer((address, port), Handler)
    try:
        print(f'http server is running at http://{address}:{port}')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down..")
        httpd.shutdown()

else:
    print(f"The file named '{args.filename}' does not exists, please create it.")

