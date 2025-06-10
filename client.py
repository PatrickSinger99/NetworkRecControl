import socket
import time
import pyautogui
from utils import *

env = load_env()
LAPTOP_IP = env["server_id"]
PORT = int(env["client_port"])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((LAPTOP_IP, PORT))
    print(f"Connected to {LAPTOP_IP} on {PORT}")

    s.sendall(b"space")
    pyautogui.hotkey('alt', 'x')
    time.sleep(137*60)
    pyautogui.hotkey('alt', 'y')
    s.sendall(b"space")
