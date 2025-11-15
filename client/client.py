import socket
import threading
import psutil
import time
import tkinter as tk
from tkinter import messagebox
from config import SERVER_PORT

root = tk.Tk()
root.title("Remote System Monitor Client")

frame_top = tk.Frame(root)
frame_top.pack(pady=5)

status_label = tk.Label(frame_top, text="Not connected")
status_label.pack()

frame_input = tk.Frame(root)
frame_input.pack(pady=5)

tk.Label(frame_input, text="Server IP:").pack(side=tk.LEFT)
server_ip_entry = tk.Entry(frame_input)
server_ip_entry.pack(side=tk.LEFT)

frame_stats = tk.Frame(root)
frame_stats.pack(pady=5)

cpu_label = tk.Label(frame_stats, text="CPU: N/A")
cpu_label.pack()
ram_label = tk.Label(frame_stats, text="RAM: N/A")
ram_label.pack()
battery_label = tk.Label(frame_stats, text="Battery: N/A")
battery_label.pack()

client_socket = None
connected = False

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery().percent if psutil.sensors_battery() else "N/A"
    return f"CPU: {cpu}% | RAM: {ram}% | Battery: {battery}", cpu, ram, battery

def update_labels(cpu, ram, battery):
    cpu_label.config(text=f"CPU: {cpu}%")
    ram_label.config(text=f"RAM: {ram}%")
    battery_label.config(text=f"Battery: {battery}")

def send_stats():
    global connected
    while connected:
        stats_str, cpu, ram, battery = get_system_stats()
        try:
            client_socket.send(stats_str.encode('utf-8'))
            update_labels(cpu, ram, battery)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            break
        time.sleep(2)

def connect_to_server():
    global client_socket, connected
    if connected:
        return

    server_ip = server_ip_entry.get()
    if not server_ip:
        messagebox.showwarning("Input Required", "Please enter the server IP")
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, SERVER_PORT))
        connected = True
        status_label.config(text=f"Connected to server {server_ip}:{SERVER_PORT}")

        threading.Thread(target=send_stats, daemon=True).start()

    except Exception as e:
        messagebox.showerror("Connection Error", str(e))

def disconnect():
    global client_socket, connected
    if connected:
        connected = False
        client_socket.close()
        status_label.config(text="Disconnected")

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="Connect", command=connect_to_server).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Disconnect", command=disconnect).pack(side=tk.LEFT, padx=5)

root.mainloop()
