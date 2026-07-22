
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


from  abc import ABC,abstractmethod
from services.gemini_services import GeminiServices
from memory.shared_memory import SharedMemory
from model.agent_response import AgentResponse
from memory.conversation_memory import ConversationMemory
from knowledge.knowledge_base import KnowledgeBase

#inherits abc class
class BaseAgent(ABC):

    def __init__(self,memory:SharedMemory,gemini_service: GeminiServices,conversation_memory:ConversationMemory=None,knowledge_base:KnowledgeBase=None):
        super().__init__()
        self.memory=memory
        self.gemini=gemini_service
        self.conversation_memory=conversation_memory if conversation_memory is not None else ConversationMemory()
        self.knowledge_base=knowledge_base if knowledge_base is not None else KnowledgeBase("data/career_knowledge.json")

   

    
    @abstractmethod
    def get_agent_name(self):
        """
        Returns to agent name 
        """
        pass

    @abstractmethod
    def get_memory_key(self):
        """
        It returns the key in which we have to store the data. 
        """
        pass

    @abstractmethod
    def build_prompt(self):
        """Build a prompt using data available in shared memory. """
        pass

   
    def execute(self)->str:
        """
        Execute the complete ai agent workflow
        build prompt->call gemini->creat agenrresource->store int memo->return resourse
        """
        agent_prompt=self.build_prompt()
        conversation=self.conversation_memory.get_context()
        knowledge=self.knowledge_base.retrieve(
            self.conversation_memory.get_context()
        )

        prompt=f"""
        conversation/context/history:{conversation}
        -----------------------------------------------
        knowledgeBase:{knowledge}
        -------------------------------------------------
        currebttask:{agent_prompt}
        
        """



        gemini_response=self.gemini.generate_response(prompt)
        #adding gemini response to conversation history
        self.conversation_memory.add_ai_message(gemini_response.text)
        agent_response=AgentResponse(
            agent_name=self.get_agent_name(),
            output=gemini_response.text,
            status="SUCCESS"
        )
        self.memory.add(
            self.get_memory_key(),
            agent_response
        )
        return agent_response

    def ask_gemini(self,prompt:str)->str:
        """Send prompt to Gemini."""

        return self.gemini.generate_response(prompt)