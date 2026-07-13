"""
Common shared memory for all the agents 
First, can store all the data from different agents. 
Second, can give data to lower-level agents to perform their actions 
Provides a common communication mechanism. 
Is independent of any specific AI agent 
"""
from typing import Any

class SharedMemory:

     def __init__(self):
          self._memory:dict[str,Any]={}
        
     def add(self,key:str,value:Any):
         """
         Add the prompt and answer of a particular agent. 
         """
         self._memory[key]=value

    
     def get(self,key:str)->str:
         """
         Gives the value of a particular prompt that is stored in shared memory 
         """
         return  self._memory.get(key)
    
     def remove(self,key:str)->None:
         """Removes a particular prompt and value from the shared memory"""

         self._memory.pop(key,None)

     def exist(self,key:str)->bool:
         """Tells whether a key exists or not"""

         return key in self._memory
    
     def clear(self)->None:
         """Clear the full shared memory."""

         self._memory.clear()


     def getAll(self)->dict[str,Any]:
         
          """Returns all the key value pairs"""

          return self._memory
    
     def display(self)->None:
        """Returns the full list."""
        print("="*50)
        print("FULL MEMORY")
        print("="*50) 

        for key,value in self._memory.items():
            print(f"{key}")
            print(value)
            print("="*50)

