
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
from model.agent_response import AgentResponse

#inherits abc class
class BaseAgent(ABC):

    def __init__(self,memory:SharedMemory):
        super().__init__(self)
        self.memory=memory
        self.gemini=GeminiServices()

   

    
    @abstractmethod
    def get_agent_name(self):
        """
        Returns to agent name 
        """
        pass

    @abstractmethod
    def get_memory_key():
        """
        It returns the key in which we have to store the data. 
        """

    @abstractethod
    def Build_Promt():
        """Build a prompt using data available in shared memory. """
        pass

   
    def execute(self)->str:
        """
        Execute the complete ai agent workflow
        build prompt->call gemini->creat agenrresource->store int memo->return resourse
        """
        prompt=self.Build_Promt()
        gemini_response=self.gemini.generate_response(prompt)
        agent_response=AgentResponse(
            agent_name=self.get_agent_name(),
            output=gemini_response.text
        )
        self.memory.add(
            self.get_memory_key,
            agent_response
        )
        return agent_response

    def ask_gemini(self,prompt:str)->str:
        """Send prompt to Gemini."""

        return self.gemini.generate_response(prompt)