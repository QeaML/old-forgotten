import json
from socket import socket

class EvalClient:
    def __init__(self):
        self.sock = socket()
        self.sock.connect(('localhost', 33780))
        
    def __call__(self, lang, src):
        data = {
            'lang':lang,
            'src':src
        }
        packet = bytes(json.dumps(data), 'utf-8')
        self.sock.send(packet)
        return self.sock.recv(8192).decode('utf-8')