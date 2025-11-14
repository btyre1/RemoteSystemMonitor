import socket
import threading

HOST = "0.0.0.0"   # Listen on all network interfaces
PORT = 5050

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    while True:
        try:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break

            print(f"[DATA FROM {addr}] {data}")

        except Exception as e:
            print(f"[ERROR] {e}")
            break

    conn.close()
    print(f"[DISCONNECTED] {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVER RUNNING] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
