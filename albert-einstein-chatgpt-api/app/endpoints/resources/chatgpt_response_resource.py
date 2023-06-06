from pydantic import BaseModel


class ChatGPTResponseResource(BaseModel):
    response: str

