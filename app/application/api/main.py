from fastapi import FastAPI


def create_app() -> FastAPI:
    return FastAPI(title="FastApi chat", docs_url="/api/docs", debug=True)
