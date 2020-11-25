"""Tiny socket server to learn how browsers, ports, ips etc
all fit together

Run in a shell and point either a browser at localhost and port or
using "nc localhost 8888 <<< GET /hello HTTP/1.1"
"""
import socketserver
from http.server import BaseHTTPRequestHandler

# I stole this response from somewhere.
generic_response = "HTTP/1.1 200 OK\r\n\nHello, world!"


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Taken from the python docs

    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())
        self.request.sendall((generic_response).encode())


if __name__ == "__main__":
    HOST, PORT = "localhost", 8888
    print(f"Listening on {HOST}:{PORT}")

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
C
