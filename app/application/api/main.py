from fastapi import FastAPI

from application.api.messages.handlers import router as message_router


def create_app() -> FastAPI:
    app = FastAPI(title="FastApi chat", docs_url="/api/docs", debug=True)
    app.include_router(message_router, prefix="/chat")
    return app
