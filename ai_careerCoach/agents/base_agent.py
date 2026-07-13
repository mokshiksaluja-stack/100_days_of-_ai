
"""
Base Agent
Every AI Agent inhertis from this class
Responsibilites:
1. Build prompt
2. Send prompt to GeminiService
3. Create AgentResponse
4. Store response in SharedMemory
5. Return AgentResponse
"""


from  abc import ABC
from services.gemini_services import GeminiServices
from memory.shared_memory import SharedMemory

#inherits abc class
class BaseAgent(ABC):

    def __init__(self,memory:SharedMemory):
        super().__init__(self)
        self.memory=memory
        self.gemini=GeminiServices()

    @abstractmethod

    def execut(self)->str:
        """
        Execute Agent 
        """
        pass

    def get_agent_name(self):
        """
        Returns to agent name """
        pass

    def get_memory_key():
        """
        It returns the key in which we have to store the data. """

    @abstractethod
    def Build_Promt():
        """Build a prompt using data available in shared memory. """
        


    def ask_gemini(self,prompt:str)->str:
        """Send prompt to Gemini."""

        return self.gemini.generate_response(prompt)