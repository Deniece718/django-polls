import os

PORT = os.environ.get("PORT", "8000")
bind = f"0.0.0.0:{PORT}"