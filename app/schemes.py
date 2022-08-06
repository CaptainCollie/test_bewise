from datetime import datetime

from pydantic import BaseModel


class QuestionsNumberRequest(BaseModel):
    questions_num: int


class Question(BaseModel):
    id: int
    question: str
    answer: str
    created: datetime
