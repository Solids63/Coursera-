import socket


class Client:
    def __init__(self, host, port, timeout=2):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self):
        with socket.create_connection((self.host, self.port)) as sock:
            sock.sendall('data'.encode('utf8'))


    def get(self):




request = Client('127.0.0.1', 8888)
print(request.put())

#  request.put()
