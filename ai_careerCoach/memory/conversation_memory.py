"""
converstaion memeory
maintains the conversation history bw the user ans ai

respo:
1.store user message 
2.store ai resoponse
3.retrieve complete conversation history
build conversation context for ai agents


"""

from typing import List

class ConversationMemory:
    """
    maintains converation history
    the stored message are later includes inside propmpts so that ai agents can 
    understand the previous conversation
    """

    def __init__(self):
        """
        initilize an empty conversation history"""
        self.message:List[str]=[]

    def add_user_message(self,message:str)->None:
        """
        Store a user message 
        Args: 
            message:userInput"""

        self.message.append(f"user: {message}")

    def add_ai_message(self,message:str)->None:
        """
        Store a ai response 
        Args: 
            message:Ai generated response"""

        self.message.append(f"AI: {message}")


    def get_context(self)->str:
        """
        rreturn the complete conversation
        Returns:
            Conversation history as a string
            
        """

        return "\n".join(self.message)
    
    def clear(self):
        """clear full history"""

        self.message.clear()

    def display(self)->None:

        """
        display the stored conversation
        usefull while debuging 
        
        """
        print("\n"+"="*60)
        print("Conersation Memorry")
        print("="*60)

        if not self.message:
            print("No conversation history")
        else:
            for message in self.message:
                print(message)
