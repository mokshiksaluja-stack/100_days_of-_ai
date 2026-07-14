
"""
reviewer agent 
it reviews and improves the carrers roadmap
"""

from agents.base_agent import BaseAgent
from prompts.reviewer_prompt import REVIEWER_PROMPT

class ReviewerAgent(BaseAgent):
    def get_agent_name(self):
        return "Reviewer"
    
    def get_memory_key(self):
        return "reviewer"
    # as key hai to small mai rakha

    def Build_Promt(self):
        writer_res=self.memory.get("writer")
        return REVIEWER_PROMPT.format(reviewer_output=writer_res)
    

    #{user_query} is a placeholder.
    # .format() replaces placeholders with actual values.
    # PLANNER_PROMPT.format(user_query=user_query) inserts the user's query into the prompt.
    # Without .format(), the placeholder remains unchanged.
    # It helps create a dynamic prompt for different users.