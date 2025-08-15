from pydantic import BaseModel, Field
from typing import Optional

class ChallengeBase(BaseModel):
    title: str
    description: Optional[str] = None
    difficulty: int = Field(ge=1, le=10)

class ChallengeCreate(ChallengeBase):
    skill_id: int  

class ChallengeUpdate(ChallengeBase):
    title: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[int] = Field(None, ge=1, le=10)
    skill_id: Optional[int] = None

class ChallengeOut(ChallengeBase):
    id: int
    skill_id: int

    class Config:
        orm_mode = True
