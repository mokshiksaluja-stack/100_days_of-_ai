# day-8 

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit(
        "Missing GEMINI_API_KEY. Add it to a .env file or export it in your shell.\n"
        "Example: GEMINI_API_KEY=your_key_here"
    )

client = genai.Client(
    api_key=api_key
)

prompt = input("enter prompt: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)