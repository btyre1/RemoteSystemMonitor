import os
from dotenv import load_dotenv

load_dotenv()

SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("SERVER_PORT", 5050))
UPDATE_INTERVAL = float(os.getenv("UPDATE_INTERVAL", 2))
LOG_FILE = os.getenv("LOG_FILE", "server/server_logs.csv")
BUFFER_SIZE = 1024
