from fastapi import FastAPI

from app.endpoints import chatgpt


def create_app():
    app = FastAPI(
        title="Albert Einstein ChatGPT Client API",
        description="Application responsible for consumes ChatGPT API",
        version="1.0.0",
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    async def on_startup() -> None:
        app.include_router(chatgpt.router, prefix="/api", tags=["chatgpt"])
    app.add_event_handler("startup", on_startup)

    return app
