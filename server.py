import socket
import pyautogui

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5005  # SEE OCCUPIED PORTS: netstat -an | findstr LISTENING


def handle_client(conn, addr):
    print(f"Connected to {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print("Client disconnected")
                break
            command = data.decode().strip()
            print(f"Received: {command}")

            if command == "start":
                screen_width, screen_height = pyautogui.size()  # Get screen size

                # Calculate target position
                target_x = screen_width - 1  # Most right pixel (0-indexed)
                target_y = screen_height // 2  # Middle of the screen vertically

                # Move the mouse and click
                pyautogui.moveTo(target_x, target_y)
                pyautogui.click(button='left')
                print("Moved and pressed on mouse")

            else:  # Basic button press
                pyautogui.press(command)
                print(f"Pressed: {command}")

    except (ConnectionResetError, BrokenPipeError):
        print("Connection lost")
    finally:
        conn.close()


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Avoid "address already in use"
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on port {PORT}")

        while True:
            conn, addr = s.accept()
            handle_client(conn, addr)


if __name__ == "__main__":
    start_server()
