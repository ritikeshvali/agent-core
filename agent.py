from openai import OpenAI
from config import API_KEY, MODEL, MAX_TOKENS_PER_REQUEST
from tools import TOOLS, search_weather, search_web
from usage_tracker import log_usage
import json

client = OpenAI(api_key=API_KEY)

def run_agent(user_question: str):
    """
    Runs the agent loop.
    
    1. Send question + tools to LLM
    2. LLM decides if it needs a tool
    3. If yes, extract tool name and params
    4. Call the tool
    5. Send result back to LLM
    6. LLM gives final answer
    """

    print(f"\nAgent received: {user_question}\n")

    messages = [
        {"role": "user", "content": user_question}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        max_tokens=MAX_TOKENS_PER_REQUEST,
        tools=TOOLS,
        tool_choice="auto",
        messages=messages
    )

    log_usage(response)

    assistant_message = response.choices[0].message

    if assistant_message.tool_calls:
        messages.append({"role": "assistant", "content": assistant_message.content, "tool_calls": assistant_message.tool_calls})

        for tool_call in assistant_message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)

            print(f"Calling tool: {tool_name}")
            print(f"Parameters: {tool_args}")

            if tool_name == "search_weather":
                result = search_weather(**tool_args)
                print(f"Result: {result}")

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
            elif tool_name == "search_web":
                result = search_web(**tool_args)
                print(f"Result: {result}")

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
        
        final_response = client.chat.completions.create(
            model=MODEL,
            max_tokens=MAX_TOKENS_PER_REQUEST,
            tools=TOOLS,
            messages=messages
        )

        log_usage(final_response)

        final_answer = final_response.choices[0].message.content
        print(f"\n Final Answer:\n{final_answer}")
    else:
        print(f"No tools needed.")
        print(f"Answer: {assistant_message.content}")

run_agent("Can I run in Delhi? What are the health benefits of running?")