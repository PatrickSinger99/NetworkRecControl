import socket
import pyautogui

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5005  # SEE OCCUPIED PORTS: netstat -an | findstr LISTENING

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on port {PORT}")
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Received: {data}")
            # pyautogui.typewrite(data)
