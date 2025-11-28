# client/config.py

# Config file for environment-driven configuration
# Avoid hardcoding sensitive or changeable settings

import os
from dotenv import load_dotenv

# Load environment variables from .env (ignore if missing)
load_dotenv()

# Network settings
SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("SERVER_PORT", 5050))
BUFFER_SIZE = int(os.getenv("BUFFER_SIZE", 1024))

# Logging settings
LOG_FILE = os.getenv("LOG_FILE", "server/server_logs.csv")

# Update interval for client
UPDATE_INTERVAL = float(os.getenv("UPDATE_INTERVAL", 2))


