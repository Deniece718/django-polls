import os

PORT = os.environ.get("PORT", "8000")
bind = f"127.0.0.1:{PORT}"