from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

hostName = '172.105.3.93'
serverPort = 80

class WebServer(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            self.path = "/index.html"

        try:

            if self.path.split(".")[-1] == "html" or self.path.split(".")[-1] == "css":
                f = open("./public" + self.path).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, "utf-8"))

            elif self.path.split(".")[-1] == "jpg":
                f = open("./public" + self.path, "rb").read()
                self.send_response(200)
                self.send_header("Content-type", "image/jpeg")
                self.end_headers()
                self.wfile.write(f)

            else:
                raise FileNotFoundError

        except FileNotFoundError as e:
            self.send_error(404, "File not found")

def run(server_class=ThreadingHTTPServer, handler_class=WebServer):
    server_address = (hostName, serverPort)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    print("Starting server on: " + hostName)
    run()