from google import genai
from dotenv import load_dotenv
import os
from datetime import datetime
import time

load_dotenv()

api=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=api)


#agent

class RoadMapAgent:
    #constructor
    def __init__(self,goal):
        #goal=userInput
        self.goal=goal
       
    #step-1 Reasoning
    def reason(self):
        print("[agent] understanding goal.....")
        prompt=f"""
        Usergoal:{self.goal}
        identify all required skills.
        Return only skills
        """

        response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    #step 2 is planing

    def planing(self,skills):
        print("[agent] planing goal.....")
        prompt=f"""
        Goal:{self.goal}
        skills:{skills}
         arrange these skills in 
        best best learning order
        """

        response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    

    #step 3 execute
    def execute(self,plan):
        print("[agent] executing plan.....")
        prompt=f"""
        Goal:{self.goal}
        learningplan:{plan}
        create a detailed suppose you are a industry expert and 
        recuriter and exactly tell students the exact and best road
        map to learn any skill
        """

        response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    

    def run(self):
        skills=self.reason()
        time.sleep(1)
        plan=self.planing(skills) 
        time.sleep(1)
        roadmap=self.execute(plan)

        print("\n" + "="*50)
        print("FINAL ROADMAP")
        print("\n" + "="*50)

        print(roadmap)

print("enter your goal")
goal=input("Goal: ")

agent=RoadMapAgent(goal)

agent.run()






