import socket
from utils import *

env = load_env()
LAPTOP_IP = env["server_id"]
PORT = env["client_port"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((LAPTOP_IP, PORT))
    s.sendall(b'Hello from PC!')
