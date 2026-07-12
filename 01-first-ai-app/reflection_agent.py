from google import genai
from dotenv import load_dotenv
import os


load_dotenv()

apikey = os.getenv("GEMINI_API_KEY")

if not apikey:
    raise ValueError("API key not found")

# Create client
client = genai.Client(api_key=apikey)

class ReflectionAgent:
    """
    Reflection Agent
    Responsibilities:
    1. Review the first draft
    2. Identify weaknesses
    3. Suggest improvements
    4. Generate improved reports
    """
    def __init__(self):
        pass


    #reviewing first draft

    def review_draft(self,draft):
        print("="*70)
        print("Reviewing Draft")
        print("="*70)

        prompt = f"""
        You are a senior AI reviewer.
        Review the following career report.
        Career Report: {draft}

        Evaluate the report on:
        1. Accuracy
        2. Completeness
        3. Clarity
        4. Practicality
        5. Missing Information
        6. Actionable Advice

        Rules:
        - Do not rewrite the report
        - Only provide feedback
        - Mention strengths
        - Mention weakness
        - Suggest improvements
"""
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )

        print("="*60)
        print("Reviewer Feedback...")
        print("="*60)
        print(response.text)
        return response.text


    def improve_draft(self, draft, feedback):
        print("="*70)
        print("Improving Draft")
        print("="*70)

        prompt = f"""
        You are Expert AI Career Consultant.
        Below is the original report:
        ---------------------
        {draft}
        ---------------------
        Reviewer Feedback:
        ---------------------
        {feedback}
        ---------------------
        Your task:
        Rewrite the report.
        Requirements:
        - Address every reviewer comment.
        - Keep the good parts
        - Improve weak sections
        - Add missing information
        - Make recommendation more practical
        - Make roadmap more actionable
"""
        
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )

        print("="*60)
        print("Improved Report...")
        print("="*60)
        print(response.text)


    #refleft
    def reflect(self, draft):
        "Draft -> Review -> Improve -> Final Report"
        
        feedback = self.review_draft(draft)
        final_report = self.improve_draft(draft, feedback)

        # return final_report
    
