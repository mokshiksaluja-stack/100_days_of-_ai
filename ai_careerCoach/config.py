"""
Configuration module 
Loads environment variables used accross the project

"""

import os

from dotenv import load_dotenv

# load_dotenv()

class Config:
    """
      central configuration class
     
    """
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
    MODEL_NAME=os.getenv("MODEL_NAME","gemini-2.5-flash")

    @staticmethod
    def validate()->None:
        """
        VAlidate Mendatory configurations

        """

        if not config.GEMINI_API_KEY:
            raise ValueError(
                "api key not found check .env file"
            )


