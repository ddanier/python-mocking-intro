from fastapi import APIRouter

from mocking_intro.module.receiver import get_answer

router = APIRouter()

@router.get("/")
def answer():
    return {
        "answer": get_answer(),
    }
