import os
import SimpleHTTPServer
import SocketServer

ip = 'localhost' # Or '127.0.0.1' instead of 'localhost'.
port = '8080' # Or '8081' or '8082' instead of '8080'.
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer((ip, int(port)), Handler)
httpd.serve_forever()