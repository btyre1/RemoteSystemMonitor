import socket
import time
import psutil  # Make sure to install: pip install psutil

SERVER_IP = "10.20.8.12"  
PORT = 5050

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery().percent if psutil.sensors_battery() else "N/A"

    data = f"CPU: {cpu}% | RAM: {ram}% | Battery: {battery}"
    return data

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))
    print("[CONNECTED TO SERVER]")

    while True:
        stats = get_system_stats()
        client.send(stats.encode('utf-8'))
        time.sleep(2)  # Send update every 2 sec

if __name__ == "__main__":
    start_client()
