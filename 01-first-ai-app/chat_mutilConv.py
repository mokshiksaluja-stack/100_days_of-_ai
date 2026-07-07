#day 9 -- creating history and giving context


# from google import genai;
# from dotenv import load_dotenv;
# import os;

# load_dotenv()

# apikey=os.getenv("GEMINI_API_KEY")

# if not apikey:
#     raise ValueError("Api key not found")

# # //creating client
# client =genai.Client(api_key=apikey)

# #store chat history

# history=[]

# system_prompt="""
# You a friendly AI chatbot response should be helpful and professional. 
# Keep answers clean and concise. Remember previous conversation context. 
# """ 

# print("="*50)
# print("chatbot")
# print("="*50)


# # creating multi connversation chatbot

# while True:

#     userInput=input("prompt:")

#     if userInput.lower() in ["byy","exit","quit"]:
#         break

#     history.append(f"user:{userInput}")

#     conContext=system_prompt+"\n"
#     conContext+="\n".join(history)


#     #call gemini
#     try:
#         response=client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=conContext
#         )

#         bot_res=response.text

#         print(f"\n Gemini:{bot_res}")

#         #store bot res

#         history.append(f"assistant:{bot_res}")
    
#     except Exception as ex:
#         print("gemini temporarly unavailable")




# //////////////////////////////////////////////////




# Day 10: Learning how to maintain the context window and generate a response using a stream. 

from google import genai
from dotenv import load_dotenv
import os
import time

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

while True:

    userInput = input("Prompt: ")

    if userInput.lower() in ["bye", "exit", "quit"]:
        print("Goodbye!")
        break

    # Store user message
    history.append(f"User: {userInput}")

    # Keep only last 20 messages
    while len(history) > MAX_HISTORY:
        history=history[-MAX_HISTORY]

    # Build conversation context
    conversation_context = system_prompt + "\n"
    conversation_context += "\n".join(history)

    fullData = ""

    startTime = time.time()

    try:
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=conversation_context
        )

        print("Gemini: ", end="")

        # If your SDK supports streaming
        for chunk in response:
            if chunk.text:
                print(chunk.text, end="", flush=True)
                fullData += chunk.text

        print()

        endTime = time.time()
        timeTaken = round(endTime - startTime, 2)
        print(f"Time for generating response: {timeTaken} sec")

        # Store assistant response
        history.append(f"Assistant: {fullData}")

        # Keep only last 20 messages
        while len(history) > MAX_HISTORY:
            history.pop(0)

    except Exception as ex:
        print("Error:")
        print(ex)