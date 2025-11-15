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

# System prompt for the agent
SYSTEM_PROMPT = """You are a helpful Weather and Information Assistant. Your role is to:

1. Help users understand weather conditions and provide running recommendations
2. Answer questions about health benefits of physical activities
3. Use available tools (search_weather, search_web) when you need current information
4. Be concise but thorough in your responses
5. Always consider safety - warn about extreme weather conditions
6. Ask clarifying questions if needed (e.g., "Which city?" or "What date?")

Important:
- Only recommend running if weather is safe
- Be honest when you don't have exact information
- Suggest checking local forecasts for critical decisions
"""