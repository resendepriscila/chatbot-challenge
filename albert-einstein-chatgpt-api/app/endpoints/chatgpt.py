from fastapi import APIRouter, status, HTTPException

from app.domain.partners.service.chatgpt_service import ChatGPTService
from app.endpoints.resources.chatgpt_request_resource import ChatGPTRequestResource
from app.endpoints.resources.chatgpt_response_resource import ChatGPTResponseResource
from app.infrastructure.core.settings import get_settings

router = APIRouter()
settings = get_settings()


@router.post("/chatgpt", status_code=status.HTTP_200_OK, response_model=list[ChatGPTResponseResource])
async def get_response(request: ChatGPTRequestResource):
    chat_service = ChatGPTService(request.prompt, request.model, request.n,
                                  request.max_tokens, request.temperature)
    try:
        return await chat_service.call_chatgpt()
    except HTTPException as exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=exception.detail)

