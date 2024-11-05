from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="Tennis Match Score Board",
        docs_url="/api/docs",
        description="Tennis Match + ddd architecture",
        debug=True,
    )

    return app
