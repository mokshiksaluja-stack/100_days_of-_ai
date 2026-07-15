"""
No agent will directly call Gemini. All the agents will come to this file, and this file will call Gemini. 
Gemini service 

"""

from google import genai
from config import Config
from typing import Any ,Optional


class GeminiServices:

    """
    Wrapper around googles gemini api
    """
    def __init__(self):
        Config.validate()
        self.client=genai.Client(api_key=Config.GEMINI_API_KEY)


    def generate_response(self,prompts:str,config:Optional[Any] = None)->Any:

        """
        Send prompt to Gemini and return response
        Args:
            prompt: Complete prompt to send
            config: Optional GenerateContentConfig
        Returns:
            AI generated response
        """

        try:
            response=self.client.models.generate_content(
            model=Config.MODEL_NAME,
            contents=prompts,
            config=config
            )
            return response

        except Exception as ex:
            raise RuntimeError(
                f"Gemini API Error : {ex}"
            )

     