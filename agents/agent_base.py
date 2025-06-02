import os
import requests
from abc import ABC, abstractmethod
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

class AgentBase(ABC):
    def __init__(self, name, max_retries=2, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.groq_api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.groq_model = os.getenv("GROQ_MODEL")    

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_llama(self, messages, temperature=0.7, max_tokens=150):
        """
        Calls the Llama model via Groq API and retrieves the response.

        Args:
            messages (list): A list of message dictionaries.
            temperature (float): Sampling temperature.
            max_tokens (int): Maximum number of tokens in the response.

        Returns:
            str: The content of the model's response.
        """
        retries = 0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[{self.name}] Sending messages to Groq API:")
                    for msg in messages:
                        logger.debug(f"  {msg['role']}: {msg['content']}")

                headers = {
                    "Authorization": f"Bearer {self.groq_api_key}",
                    "Content-Type": "application/json"
                }
                data = {
                    "model": self.groq_model,
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens
                }
                response = requests.post(self.groq_api_url, headers=headers, json=data, timeout=60)
                response.raise_for_status()
                reply = response.json()["choices"][0]["message"]["content"]

                if self.verbose:
                    logger.info(f"[{self.name}] Received response: {reply}")

                return reply
            except Exception as e:
                retries += 1
                logger.error(f"[{self.name}] Error during Groq API call: {e}. Retry {retries}/{self.max_retries}")
        raise Exception(f"[{self.name}] Failed to get response from Groq API after {self.max_retries} retries.")
