from pydantic import BaseModel


class ChatGPTRequestResource(BaseModel):

    prompt: str
    model: str
    n: int
    max_tokens: int
    temperature: int


