

from google import genai
from dotenv import load_dotenv
import os
import time
from datetime import datetime
import random

load_dotenv()

apikey = os.getenv("GEMINI_API_KEY")

if not apikey:
    raise ValueError("API key not found")

# Create client
client = genai.Client(api_key=apikey)

# Store chat history
history = []
MAX_HISTORY = 20

system_prompt = """
You are a friendly AI chatbot. Responses should be helpful and professional.
Keep answers clean and concise. Remember previous conversation context.
"""

print("=" * 50)
print("Chatbot")
print("=" * 50)

def get_time():
    return datetime.now().strftime("%I:%M:%S,%p")

def motivation():
    quotes=[
        "consistency 11","consistency 22","consistency 33","consistency 44","consistency 55"
    ]

    return random.choice(quotes)
    

def tool_routes(query):
    query.lower
    if "time" in query:
        return "time"
    elif "motivation"in query or "quotes" in query:
        return "quotes"

while True:

    userInput = input("Prompt: ")
    history.append(f"User: {userInput}")
    while len(history) > MAX_HISTORY:
        history=history[-MAX_HISTORY]

    conversation_context = system_prompt + "\n"
    conversation_context += "\n".join(history)

    if userInput.lower() in ["bye", "exit", "quit"]:
        print("Goodbye!")
        break

    tool=tool_routes(userInput)

    if tool=="time":
         print(get_time())

    elif tool=="quotes":
        print(motivation())
    
    else:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation_context
        )
        print(f"gemini{response.text}")


   
    
 
    

    