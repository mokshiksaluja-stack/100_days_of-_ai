"""
to give a sequence of execution to agents as an orchestrator just like a man holding stich and guide fellow mussicians

"""
from typing import List,Dict
from agents.base_agent import BaseAgent
from memory.shared_memory import SharedMemory
from model.agent_response import AgentResponse



class AgentOrchestrator:
    MAX_RETRIES=3
    def __init__(self,memory:SharedMemory,conversation_memory):
        self.memory=memory
        self.agents:List[BaseAgent]=[]
        self.conversation_memory=conversation_memory
        self.agents:Dict[str,BaseAgent]={}

    def registry(self,agent):
        """
        register the agents
        """
        # self.agents.append(agent)
        self.agents[agent.get_agent_name().lower()]=agent

    # def execute(self):
    #     print("\nStarting Multi-Agent Workflow....")
    #     """execute agents sequently"""
    #     for agent in self.agents:
    #         print(f"executing {agent.get_agent_name()} Agent...")
    #         response=agent.execute()
    #         print(f"{response.agent_name} executed successfully")
        
    #     print("WorkFlow Completed")
    #     return self.memory.get("reviewer")


    def execute(self,workflow:List[str])->AgentResponse:
        """
        Execute the selected workflow
        Args:
            workflow: Ordered list of agent names
        
        Returns:
            Final AgentResponse
        """
        print("\n starting Multi-Agent Workflow...")

        final_response=None

        for step,agent_name in enumerate(workflow,start=1):
            agent=self.agents.get(agent_name.lower())

            if agent is None:
                raise ValueError (f"Agent {agent_name} is not register")
            print(f"\n Step:{step}:Executing{agent.get_agent_name()} Agent....")

            # final_response=agent.execute()
            final_response=self._execute_with_retry(agent)


            print(f"{agent.get_agent_name} completed successfully")

        print("Workflow Completed")
        return final_response
    

    def _execute_with_retry(self,agent:BaseAgent)->AgentResponse:
        """
        execute an ai agent with retry mechanisnmn"""

        for attempt in range(1,self.MAX_RETRIES+1):

            try:
                print(f"Attempt {attempt}")
                response=agent.execute()
                print("Success")
                return response
            except Exception as ex:
                print(f"Attempt {attempt} failed...")
                print(ex)

                if attempt ==self.MAX_RETRIES:
                    raise RuntimeError(
                        f"{agent.get_agent_name()} failed after"
                        f"{self.MAX_RETRIES} retries..."
                    )
                print("Retring")


    
    
