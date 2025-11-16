import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import time
import csv
from config import SERVER_HOST, SERVER_PORT, LOG_FILE, BUFFER_SIZE

# Keep track of currently connected clients
active_clients = []

# --- GUI Setup ---
root = tk.Tk()
root.title("Remote System Monitor Server")

# Top frame for status and client count
frame_top = tk.Frame(root)
frame_top.pack(padx=10, pady=5)

# Status label shows server state
status_label = tk.Label(frame_top, text="Server is starting...")
status_label.pack()

# Number of currently active clients
clients_label = tk.Label(frame_top, text="Active Clients: 0")
clients_label.pack()

# Scrollable text area for server log messages
log_area = ScrolledText(root, width=70, height=20)
log_area.pack(padx=10, pady=10)

# --- Logging helper ---
def log(message):
    """
    Append messages to the GUI log with a timestamp.
    Keeping logs in the GUI allows monitoring without terminal output.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_area.insert(tk.END, f"[{timestamp}] {message}\n")
    log_area.see(tk.END)  # Scroll to the latest message


# --- Client handler ---
def handle_client(conn, addr):
    """
    Receives data from a client and logs it.
    Each client gets its own thread to prevent blocking others.
    """
    log(f"NEW CONNECTION: {addr} connected")
    active_clients.append(addr)
    clients_label.config(text=f"Active Clients: {len(active_clients)}")

    try:
        while True:
            # Receive data from the client
            data = conn.recv(BUFFER_SIZE).decode()
            if not data:
                break  # Client disconnected

            log(f"DATA FROM {addr}: {data}")

            # Persist the data to a CSV log
            with open(LOG_FILE, "a") as f:
                csv.writer(f).writerow([addr, data, time.strftime("%Y-%m-%d %H:%M:%S")])

    except Exception as e:
        log(f"ERROR: {e}")  # Catch network errors or decode errors

    finally:
        # Clean up connection and GUI
        conn.close()
        active_clients.remove(addr)
        clients_label.config(text=f"Active Clients: {len(active_clients)}")
        log(f"DISCONNECTED: {addr}")

# --- Server starter ---
def start_server():
    """
    Start the TCP server, accept incoming client connections,
    and spawn a new thread for each client.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((SERVER_HOST, SERVER_PORT))  # Bind to host and port
        server.listen()  # Listen for incoming connections
        status_label.config(text=f"Server Running on {SERVER_HOST}:{SERVER_PORT}")
    except Exception as e:
        log(f"SERVER ERROR: {e}")
        return

    while True:
        conn, addr = server.accept()  # Wait for a new client
        # Handle each client in a separate daemon thread
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

# Run server in background so GUI remains responsive
threading.Thread(target=start_server, daemon=True).start()
root.mainloop()

