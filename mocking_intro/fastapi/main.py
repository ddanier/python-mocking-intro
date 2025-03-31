from fastapi import FastAPI

from .routes.answer import router as answer_router

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello world",
    }


app.include_router(answer_router, prefix="/answer")
