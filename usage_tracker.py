from datetime import datetime
from config import USAGE_LOG_FILE, TRACK_USAGE

def log_usage(response):
    """Log API usage to file"""
    if not TRACK_USAGE:
        return
    
    usage = response.usage
    log_entry = f"[{datetime.now()}] Tokens: Input={usage.prompt_tokens}, Output={usage.completion_tokens}, Total={usage.total_tokens}\n"

    with open(USAGE_LOG_FILE, "a") as f:
        f.write(log_entry)

    print(f"Usage tracked: {usage.total_tokens} tokens total")

def get_total_usage():
    """Read total tokens from log"""
    try:
        with open(USAGE_LOG_FILE, "r") as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0