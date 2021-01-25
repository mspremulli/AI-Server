import http.server
import socketserver

with socketserver.TCPServer(("", 8003), http.server.SimpleHTTPRequestHandler) as http:
    print("connected")
    http.serve_forever()

