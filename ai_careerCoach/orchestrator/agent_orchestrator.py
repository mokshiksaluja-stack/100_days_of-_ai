"""
Agent Orchestrator
Responsible for managing the execution of AI Agents

Responsibilities:
1. Register AI Agents
2. Execute selected workflow
3. Retry failed agents
4. Track execution details
5. Return the final response
"""



from typing import List,Dict
from agents.base_agent import BaseAgent
from memory.shared_memory import SharedMemory
from model.agent_response import AgentResponse
from model.agent_execution_result import AgentExecutionResult
from memory.conversation_memory import ConversationMemory
from concurrent.futures import ThreadPoolExecutor
import time



class AgentOrchestrator:
    MAX_RETRIES=3
    def __init__(self,memory:SharedMemory,conversation_memory=None):
        self.memory=memory
        self.conversation_memory=conversation_memory if conversation_memory is not None else ConversationMemory()
        self.agents:Dict[str,BaseAgent]={}
        self._execution_results:List[AgentExecutionResult]=[]
        self._approval_required_agents={
            "reviewer"
        }

    def register(self,agent):
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

        self._execution_results.clear()

        final_response=None

        for step,agent_name in enumerate(workflow,start=1):
            

            # parallel execution
            if isinstance(agent_name,List):
                parallel_res=self._execute_parallel(agent_name)
                if parallel_res:
                    final_response=parallel_res[-1] #pushed last idx of this

            #sequential execution
            else:
                agent=self.agents.get(agent_name.lower())

                if agent is None:
                    raise ValueError (f"Agent {agent_name} is not register")
                print(f"\n Step:{step}:Executing{agent.get_agent_name()} Agent....")


                #human approval required
                if agent_name.lower() in self._approval_required_agents:
                    approved =self._request_human_approval(agent)

                    if not approved:

                        print(f"{agent.get_agent_name()} execution cancelled")
                    
                        self._execution_results.append(
                        AgentExecutionResult(
                            agent_name=agent.get_agent_name(),
                            status="SKIPPED",
                            attempts=0,
                            execution_time=0.0,
                            error_message="Execution rejected by user"   
                            )
                        )
                        print("workflow stoped by user ")
                        break



                # final_response=agent.execute()
                final_response=self._execute_with_retry(agent)


                print(f"{agent.get_agent_name()} completed successfully")

        print("Workflow Completed")
        return final_response
        
    


    def _execute_with_retry(self,agent:BaseAgent)->AgentResponse:
        """
        execute an ai agent with retry mechanisnmn"""

        start_time=time.perf_counter()
        last_exception=None

        for attempt in range(1,self.MAX_RETRIES+1):

            try:
                print(f"Attempt {attempt}")
                response=agent.execute()
                execution_time= (time.perf_counter()-start_time)
                self._execution_results.append(
                    AgentExecutionResult(
                        agent_name=agent.get_agent_name(),
                        status="SUCCESS",
                        attempts=attempt,
                        execution_time=execution_time   
                    )
                )
                print("Success")
                return response
            except Exception as ex:
                last_exception=ex
                print(f"Attempt {attempt} failed...")
               

                if attempt<self.MAX_RETRIES:
                    print("Retring")


        execution_time=(time.perf_counter()-start_time)
        self._execution_results.append(
            AgentExecutionResult(
                agent_name=agent.get_agent_name(),
                status="Failed",
                attempts=self.MAX_RETRIES,
                execution_time=execution_time,
                error_message=str(last_exception )    
            )
        )

        raise RuntimeError(
            f"{agent.get_agent_name()}"
            f"after {self.MAX_RETRIES} attempts"
        )from last_exception
    

    
    #humam in loop/approval
    def _request_human_approval(self, agent: BaseAgent) -> bool:
        """
        Ask the user for approval before executing a critical AI Agent.
        
        Args:
            agent:
                Agent requiring approval
        
        Returns:
            True if approved
            False otherwise
        """
        print("=" * 70)
        print("HUMAN APPROVAL REQUIRED")
        print("=" * 70)

        print(f"{agent.get_agent_name()} Agent requires manual approval")

        while True:
            choice = input("Approve execution ? (Y/N): ").strip().lower()
            if choice == "y":
                return True
            
            if choice == "n":
                return False
            
            print("Invalid input. Please enter Y or N.")

    def _execute_parallel(self,agent_names:List[str]):
        print("\n Executing Parallel Agents.... \n")

        with ThreadPoolExecutor(max_workers=len(agent_names)) as executor:
            futures=[]
            for agent_name in agent_names:
                agent=self.agents[agent_name.lower()]
                futures.append(
                    executor.submit(self._execute_with_retry,agent)
                )

            responses=[]
            
            for future in futures:
                responses.append(future.result())


            return responses



    def get_execution_results(self) -> List[AgentExecutionResult]:
        """
        Return execution summary
        """
        return self._execution_results
    
    def display_execution_summary(self) -> None:
        """
        Display execution summary
        """
        print("=" * 70)
        print("AGENT EXECUTION SUMMARY")
        print("=" * 70)

        for result in self._execution_results:
            result.display()
            print("-" * 70)

        print("=" * 70)
    


    
    
