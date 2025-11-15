# Read configuration values from environment (.env recommended).
# Using python-dotenv allows easy local .env files while keeping code config-driven.

import os
from dotenv import load_dotenv

# load .env if present (no error if not)
load_dotenv()

# defaults are safe for local testing
SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("SERVER_PORT", 5050))
UPDATE_INTERVAL = float(os.getenv("UPDATE_INTERVAL", 2.0))
LOG_FILE = os.getenv("LOG_FILE", "server/server_logs.csv")
