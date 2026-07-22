
"""
writer agent 
converts research into a professional roadmap
"""

from agents.base_agent import BaseAgent
from prompts.writer_prompt import WRITER_PROMPT

class WriterAgent(BaseAgent):
    def get_agent_name(self):
        return "Writer"
    
    def get_memory_key(self):
        return "writer"
    # as key hai to small mai rakha

    def build_prompt(self):
        research_res=self.memory.get("researcher")
        return WRITER_PROMPT.format(research_output=research_res.output)
    

    #{user_query} is a placeholder.
    # .format() replaces placeholders with actual values.
    # PLANNER_PROMPT.format(user_query=user_query) inserts the user's query into the prompt.
    # Without .format(), the placeholder remains unchanged.
    # It helps create a dynamic prompt for different users.