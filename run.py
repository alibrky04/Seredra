import uvicorn
from seredra.api.routes import router
from seredra.db.database import init_db
from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title="Seredra Weather API",
        description="A simple, functional weather information SaaS.",
        version="0.1.0"
    )
    app.include_router(router)
    return app

app = create_app()

if __name__ == "__main__":
    init_db()
    uvicorn.run("run:app", host="0.0.0.0", port=8000, reload=True)
