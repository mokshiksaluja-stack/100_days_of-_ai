#with orchestration

"""

AI Career Coach
Entry point of the application
"""

from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

from orchestrator.agent_orchestrator import AgentOrchestrator

from routing.workflow_registry import WorkflowRegistry
from routing.workflow_router import WorkflowRouter


from services.gemini_services import GeminiServices

from memory.shared_memory import SharedMemory
from memory.conversation_memory import ConversationMemory
from knowledge.knowledge_base import KnowledgeBase

def main() :
    conversation_memory=ConversationMemory()
    gemini_service = GeminiServices()
    knowledge_base=KnowledgeBase("./data/career_knowledge.json")

    workflow_registry=WorkflowRegistry()
    workflow_router=WorkflowRouter(gemini_service,workflow_registry)


    while True:
        print("=" * 70)
        print("AI Career Coach")
        print("=" * 70)

        user_query = input("Enter your career goal : \n")
        if user_query.lower == "exit" or "byy" or "quit":
            break

        conversation_memory.add_user_message(user_query)
        
        # Initialize shared components
        memory = SharedMemory()
        
        
        
        # Store user query
        memory.add("user_query", user_query)


        # Create Agents
        planner = PlannerAgent(memory, gemini_service,conversation_memory,knowledge_base)
        researcher = ResearchAgent(memory, gemini_service,conversation_memory,knowledge_base)
        writer = WriterAgent(memory, gemini_service,conversation_memory,knowledge_base)
        reviewer = ReviewerAgent(memory, gemini_service,conversation_memory,knowledge_base)

        orc=AgentOrchestrator(memory,conversation_memory)
        orc.registry(planner)
        orc.registry(researcher)
        orc.registry(writer)
        orc.registry(reviewer)

        

        # conversation_memory.display()

        #Route user,s request

        decision=workflow_router.route(user_query)
        decision.display()

        #retrive the workflow
        workflow=workflow_registry.get_workFlow(decision.workflow_name)


        for index,agent in enumerate(workflow,start=1):
            print(f"{index}.{agent.title()}Agent")

        final_response = orc.execute(workflow)

        print("="*70)
        print("FINAL CAREER ROADMAP")
        print("="*70)
        print(final_response.output)


    if __name__ == "__main__":
        main()