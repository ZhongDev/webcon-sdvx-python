# begin imports
# import general libraries
import os
# import http server libraries
import http.server
import socketserver

# http server configurations
HTTPPORT = 8080
web_dir = os.path.join(os.path.dirname(__file__), 'html')
os.chdir(web_dir)
Handler = http.server.SimpleHTTPRequestHandler

# http server
with socketserver.TCPServer(("", HTTPPORT), Handler) as httpd:
    print("HTTP Server is active at localhost:8080")
    httpd.serve_forever()
