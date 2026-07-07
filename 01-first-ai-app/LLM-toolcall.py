

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


system_prompt = """
You are a friendly AI chatbot. Responses should be helpful and professional.
Keep answers clean and concise. Remember previous conversation context.
"""

print("=" * 50)
print("Chatbot")
print("=" * 50)

def get_time(query=None):
    return datetime.now().strftime("%I:%M:%S,%p")

def motivation(query=None):
    quotes=[
        "consistency 11","consistency 22","consistency 33","consistency 44","consistency 55"
    ]

    return random.choice(quotes)

def roadmap(skill):
    prompt= f"""
    for {skill} provide me a 10 day revision roadmap
    """
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print(response.text)



TOOL={
    "time_tool":get_time,
    "motivation_tool":motivation,
    "roadmap_tool":roadmap
}

def select_tool(query):
    prompt = f"""
    suppose you are a tool selector. Available tools are:
    - time_tool
    - motivation_tool
    - roadmap_tool
    - return only tool name
     userquery:{query}

    """
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        )
    tool_name = response.text.strip()
    print(f"assistant:{tool_name} tool is selected")
    return tool_name



def execute_tool(tool_name,query):
    tool1=TOOL.get(tool_name)

    if not tool1:
        return "tool not found"

    return tool1(query)# calling the exact tool

while True:

    userInput = input("Prompt: ")
   
   

    

    if userInput.lower() in ["bye", "exit", "quit"]:
        print("Goodbye!")
        break


    tool=select_tool(userInput)
    print(f"tool selected is {tool}")

    result=execute_tool(tool,userInput)
    print(f"\n assistant:{result}")

   

    
    

   
    
 
    

    