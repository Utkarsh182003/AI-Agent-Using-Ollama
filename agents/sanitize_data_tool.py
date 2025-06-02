from .agent_base import AgentBase

class SanitizeDataTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SanitizeDataTool", max_retries=max_retries, verbose=verbose)

    def execute(self, medical_data):
        messages = [
            {"role": "system", "content": "You are an AI assistant that sanitizes data by removing unnecesaary information or foul language."},
            {
                "role": "user",
                "content": (
                    "Remove all unnecesaary information or foul language from the following data:\n\n"
                    f"{medical_data}\n\nSanitized Data:"
                )
            }
        ]
        sanitized_data = self.call_llama(messages, max_tokens=500)
        return sanitized_data
