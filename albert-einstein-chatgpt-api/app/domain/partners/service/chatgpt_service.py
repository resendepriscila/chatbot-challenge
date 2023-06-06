import openai

from app.endpoints.resources.chatgpt_response_resource import ChatGPTResponseResource
from app.infrastructure.core.settings import get_settings

settings = get_settings()


class ChatGPTService:
    def __init__(self, prompt, model, number, max_tokens, temperature):
        self.prompt = prompt
        self.model = model
        self.n = number
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.key = settings.chatgpt_api_token
        self.echo = True
        openai.api_key = settings.chatgpt_api_token

    async def call_chatgpt(self):
        response = openai.Completion.create(
            model=self.model,
            prompt=self.prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            n=self.n,
        )
        responses = []
        for choice in response.choices:
            responses.append(ChatGPTResponseResource(response=choice.text))
        return responses
