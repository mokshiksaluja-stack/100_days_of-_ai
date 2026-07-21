
"""
research agent 
performs detailed research on the planners roadmap
"""

from agents.base_agent import BaseAgent
from prompts.research_prompt import RESEARCH_PROMPT

class ResearchAgent(BaseAgent):
    def get_agent_name(self):
        return "Researcher"
    
    def get_memory_key(self):
        return "researcher"
    # as key hai to small mai rakha

    def Build_Promt(self):
        planner_res=self.memory.get("planner")
        return RESEARCH_PROMPT.format(planner_output=planner_res.output)
    

    #{user_query} is a placeholder.
    # .format() replaces placeholders with actual values.
    # PLANNER_PROMPT.format(user_query=user_query) inserts the user's query into the prompt.
    # Without .format(), the placeholder remains unchanged.
    # It helps create a dynamic prompt for different users.