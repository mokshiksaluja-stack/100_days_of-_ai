"""
Workflow Router

Uses Gemini to intelligently select the most appropriate 
workflow for user's request

Responsibilities:
1. Build the routing prompt
2. Retrieve available workflows from Registry
3. Ask Gemini to classify the request
4. Return Workflow Decision
"""


from services.gemini_services import GeminiServices
from routing.workflow_registry import WorkflowRegistry
from model.workflow_decision import WorkFlowDecision

from google.genai import types


class WorkflowRouter:
    """
    LLM-Powered workflow router
    Gemini analyzes the user's request and select the most appropriate workflow
    """

    def __init__(self, gemini_service: GeminiServices, 
                 workflow_registry: WorkflowRegistry) -> None:
        """
        Initialize workflow Router
        """

        self.gemini = gemini_service
        self.registry = workflow_registry

    def route(self,user_query:str)->WorkFlowDecision:
        """
        Route the user query.
        Args:
            user_query: User request
        
        Returns:
            WorkflowDecision
        """
         
        prompt=self.build_prompt(user_query)
        response = self.gemini .generate_response(
            prompt=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=WorkFlowDecision
            )
        )

        return response.parsed
    
    
    def build_prompt(self,user_query:str)->str:
        """
        Build the routing prompt
        Args:
            user_query: User request
        
        Returns:
            Prompt string
        
        """

        work_details=[]
        for wk in self.registry.get_available_workflows():
            work_details.append(f"-{wk}")

        available_wk="\n".join(work_details)

        #its output
        """
        roadmap- workflow
        certification- workflow
        project- workflow
        review- workflow
        """

        prompt = f"""
        You are an enterprise AI workflow router.
        Your job is to determine which workflow should execute.
        Available workflows:
        {available_wk}

        Instructions:
        1. Select ONLY ONE Workflow
        2. Return your answer using the provided schema.
        3. Do NOT explain anything
        
        User Request:
        {user_query}
"""
        return prompt
         
        
         

