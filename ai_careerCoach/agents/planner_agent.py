"""
create the initial career learning plan 
"""

from agents.base_agent import BaseAgent
from prompts.planner_prompt import PLANNER_PROMPT

class PlannerAgent(BaseAgent):
    def get_agent_name(self):
        return "Planner"
    
    def get_memory_key(self):
        return "planner"
    # as key hai to small mai rakha

    def build_prompt(self):
        user_query=self.memory.get("user_query")
        return PLANNER_PROMPT.format(user_query=user_query)
    

    #{user_query} is a placeholder.
    # .format() replaces placeholders with actual values.
    # PLANNER_PROMPT.format(user_query=user_query) inserts the user's query into the prompt.
    # Without .format(), the placeholder remains unchanged.
    # It helps create a dynamic prompt for different users.