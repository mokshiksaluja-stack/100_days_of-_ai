"""
Workflow Decision
Represents the routing decision returned by the Workflow Router

Responsibilities:
1. Store the selected workflow
2. Store routing confidence
3. Store the reason for selecting the workflow
"""


from dataclasses import dataclass

@dataclass
class WorkFlowDecision:
    workflow_name:str
    confidence:str
    reason:str

    def display(self)->None:
        
        """
        Display the workflow decision
        """
        print("=" * 70)
        print("WORKFLOW DECISION")
        print("=" * 70)

        print("Workflow :", self.workflow_name)
        print("Confidence :",self.confidence)
        print("Reason :",self.reason)
        print("=" * 70)



# data class replace init as we dont have to initilize variables