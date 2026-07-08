from google import genai
from google.genai import types
from dotenv import load_dotenv
import os


load_dotenv()

apikey = os.getenv("GEMINI_API_KEY")

if not apikey:
    raise ValueError("API key not found")

# Create client
client = genai.Client(api_key=apikey)


print("=" * 50)
print("Gemini for carrer roadmap- skill certificate and salary")
print("=" * 50)

def get_skill(role: str):
    """
    Returns required skills for a role.
    Parameters:Role (str)-Career Role selected by user
    Return :Dict: Required Skills
    """

    return{
        "role":role,
        "skills":[
            "python","machineLearning","datta Science", "deep learning","llms"
        ]
    }

def get_certifications(role:str):
    """
    Return certificate info
    parameters: role(str): career role
    returns:dict
    """

    return{
        "role":role,
        "certifications":["ai-102","az-104","dp300","aws cloud practitioner "]
    }

def get_salary(role:str):
    """
    Returns expected salary range 
    parameters: role (str)
    returns: dict
    """

    return{
        "role":role,
        "salary":"15-20lpa"
    }


Tools=[get_salary,get_certifications,get_skill]


query=input("promt: ")

response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=query,
    config=types.GenerateContentConfig(
        tools=Tools
    )

)

print(response.text)


     