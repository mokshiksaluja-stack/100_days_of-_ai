"""
to give a sequence of execution to agents as an orchestrator just like a man holding stich and guide fellow mussicians

"""
from typing import List
from agents.base_agent import BaseAgent
from memory.shared_memory import SharedMemory


class AgentOrchestrator:
    def __init__(self,memory:SharedMemory):
        self.memory=memory
        self.agents:List[BaseAgent]=[]

    def registry(self,agent):
        """
        register the agents
        """
        self.agents.append(agent)

    def execute(self):
        print("\nStarting Multi-Agent Workflow....")
        """execute agents sequently"""
        for agent in self.agents:
            print(f"executing {agent.get_agent_name()} Agent...")
            response=agent.execute()
            print(f"{response.agent_name} executed successfully")
        
        print("WorkFlow Completed")
        return self.memory.get("reviewer")
