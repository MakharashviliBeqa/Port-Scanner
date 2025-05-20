import socket
import threading
from queue import Queue

target = "127.0.0.1"
queue = Queue()
open_ports = []

def portscanner(port):
    try :
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except :
        return False

for port in range(1, 1025):
    result = portscanner(port)
    if result:
        print(f"Port {port} is open".format(port))
    else:
        print(f"Port {port} is closed".format(port))