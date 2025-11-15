import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment file.")

MODEL = "gpt-4o-mini"

# Safety Limits
MAX_TOKENS_PER_REQUEST = 1000
MAX_API_CALLS_PER_SESSION = 50
REQUEST_TIMEOUT_SECONDS = 30

# Rate limiting
REQUESTS_PER_MINUTE = 5
MAX_INPUT_TOKENS_PER_MINUTE = 10000

# Usage Tracking
USAGE_LOG_FILE = "usage_log.txt"
TRACK_USAGE = True