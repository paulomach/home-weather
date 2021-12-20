"""Logger function."""
from datetime import datetime as dt


def log(message):
    """Log to the console."""
    print(f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}: {message}")
