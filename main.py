from openai import OpenAI
from config import API_KEY, MODEL, MAX_TOKENS_PER_REQUEST
from usage_tracker import log_usage

client = OpenAI(api_key=API_KEY)

message_content = "What's a good time to go for a run tomorrow?"

response = client.chat.completions.create(
    model=MODEL,
    max_tokens=MAX_TOKENS_PER_REQUEST,
    messages=[
        {
            "role": "user",
            "content": message_content
        }
    ]
)

# Track usage
log_usage(response)

print(response.choices[0].message.content)