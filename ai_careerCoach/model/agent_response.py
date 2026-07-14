"""
agent response model
represent the standardized response returned by every ai agent.
"""
from dataclasses import dataclass,field
from datetime import datetime
from typing import Optional

@dataclass
class AgentResponse:
    """
    standard response return by every ai agent
    """
    #name of ai agent
    agent_name:str

    #ai generated output
    output:str

    #execution status of agent
    status:str

    #error message (if any)
    error: Optional[str]=None

    #Response Generation time 
    timestamp:datetime=field(
        default_factory=datetime.now
    )

    def is_success(self)->bool:
        """
        return true if execution was successfull'
        """

        return self.status.upper()=="SUCCESS"
    


    #this methode is just like toString in java  here we 
    # use __str__ for structured string output
    
    def __str__(self):
        """
        Pretty string representation
        """

        return (
            f"\nAgent:{self.agent_name}"
            f"\nStatus:{self.status}"
            f"\nTimeStamp:{self.timestamp}"
            f"\nOutput:{self.output}"
        )
    


#     Without @dataclass

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# We have to manually create the constructor and assign values.

# With @dataclass

# from dataclasses import dataclass

# @dataclass
# class Student:
#     name: str
#     age: int

# Python automatically creates the constructor.

# Why use it?

# ✅ Less code to write

# ✅ Cleaner and easier to read

# ✅ Good for classes that only store information

# ✅ Python automatically creates useful methods like __init__()

# In AgentResponse

# The class is only storing:

# agent name
# output
# status
# error
# timestamp

# So @dataclass is used because this class is mainly a data container.

# Easy Interview Answer

# A dataclass is used to reduce boilerplate code in classes that mainly store data. It automatically generates methods like __init__() and makes the code cleaner and easier to maintain.