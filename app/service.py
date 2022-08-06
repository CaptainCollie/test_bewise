from typing import Optional

import requests
from sqlmodel import select, col
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models import Questions
from app.schemes import Question


async def add_questions(session: AsyncSession,
                        questions_num: int) -> Optional[Question]:
    questions = await get_unique_questions(session, questions_num)
    questions = [Questions(question=q["question"],
                           answer=q["answer"],
                           created=q["created_at"]) for q in questions]
    for q in questions:
        q.created = q.created.replace(tzinfo=None)

    query = select(Questions).order_by(col(Questions.created_at).desc())
    prev_question = (await session.execute(query)).first()
    if prev_question:
        prev_question = prev_question[0]
        prev_question = Question(
            id=prev_question.id,
            question=prev_question.question,
            answer=prev_question.answer,
            created=prev_question.created
        )

    for q in questions:
        session.add(q)
    await session.commit()
    return prev_question


async def check_exist(session: AsyncSession,
                      question: str) -> bool:
    query = select(Questions).where(Questions.question == question)
    result = await session.scalar(query)
    return True if result else False


async def get_unique_questions(session: AsyncSession,
                               questions_num: int) -> list[dict]:
    questions_url = "https://jservice.io/api/random"
    non_exist_questions = []
    request_num = questions_num
    while len(non_exist_questions) != questions_num:
        response = requests.get(questions_url, params={"count": request_num})
        questions = response.json()
        questions = [question for question in questions if
                     not await check_exist(session, question["question"])]
        request_num -= len(questions)
        non_exist_questions.extend(questions)
    return non_exist_questions


async def get_questions(session: AsyncSession) -> list[Question]:
    query = select(Questions)
    results = await session.exec(query)
    results = [Question(id=result.id,
                        question=result.question,
                        answer=result.answer,
                        created=result.created) for result in results]
    return results
