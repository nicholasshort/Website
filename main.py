from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import socket
import os

from api import GithubAPI

hostName = socket.gethostbyname(socket.gethostname())
serverPort = 80

class WebServer(BaseHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        if self.path == "/":
            self.path = "/index.html"

        try:
            
            if self.path.split(".")[-1] == "html" or self.path.split(".")[-1] == "css":
                
                # Get html from github api
                if self.path == '/projects.html':
                    
                    content = open('./public/projects.html').read()
                    
                    api = GithubAPI('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', 'nicholasshort')
                    repos = api.get_starred_repo_names()
                    
                    for repo in repos:
                        content = content + '<h2>' + repo + '</h2>'
                        content = content + api.get_readme(repo).content.decode("utf-8")
                        content = content + '<br><br><br><br>'

                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(bytes(content, "utf-8"))
                
                # Static files (no api)  
                else:
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
                raise Exception()

        except:
            self.send_error(404, "File not found")

def run(server_class=ThreadingHTTPServer, handler_class=WebServer):
    server_address = (hostName, serverPort)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    print(hostName)
    run()

