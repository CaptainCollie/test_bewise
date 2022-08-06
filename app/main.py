from typing import Optional

from fastapi import FastAPI, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session
from app.schemes import QuestionsNumberRequest, Question
from app.service import get_questions as get_q, add_questions as add_q

app = FastAPI()


@app.post('/questions', response_model=Optional[Question])
async def add_questions(questions_number: QuestionsNumberRequest,
                        session: AsyncSession = Depends(get_session)):
    result = await add_q(session, questions_number.questions_num)
    print('result', result)
    return result


@app.get('/questions', response_model=list[Question])
async def get_questions(session: AsyncSession = Depends(get_session)):
    return await get_q(session)
