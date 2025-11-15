import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import time
import csv

HOST = "0.0.0.0"
PORT = 5050
BUFFER_SIZE = 1024
active_clients = []

root = tk.Tk()
root.title("Remote System Monitor Server")

frame_top = tk.Frame(root)
frame_top.pack(padx=10, pady=5)

status_label = tk.Label(frame_top, text="Server is starting...")
status_label.pack()

clients_label = tk.Label(frame_top, text="Active Clients: 0")
clients_label.pack()

log_area = ScrolledText(root, width=70, height=20)
log_area.pack(padx=10, pady=10)

def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_area.insert(tk.END, f"[{timestamp}] {message}\n")
    log_area.see(tk.END)

def handle_client(conn, addr):
    log(f"NEW CONNECTION: {addr} connected")
    active_clients.append(addr)
    clients_label.config(text=f"Active Clients: {len(active_clients)}")
    while True:
        try:
            data = conn.recv(BUFFER_SIZE).decode('utf-8')
            if not data:
                break
            log(f"DATA FROM {addr}: {data}")
            with open("server_logs.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([addr, data, time.strftime("%Y-%m-%d %H:%M:%S")])
        except Exception as e:
            log(f"ERROR: {e}")
            break
    conn.close()
    active_clients.remove(addr)
    clients_label.config(text=f"Active Clients: {len(active_clients)}")
    log(f"DISCONNECTED: {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    status_label.config(text=f"Server Running on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

threading.Thread(target=start_server, daemon=True).start()
root.mainloop()