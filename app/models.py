from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Questions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question: str = Field(index=True)
    answer: str
    created: datetime
    created_at: datetime = Field(default_factory=datetime.utcnow,
                                 nullable=False)
