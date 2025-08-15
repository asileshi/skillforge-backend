from pydantic import BaseModel, Field
from typing import Optional

class ChallengeBase(BaseModel):
    title: str
    description: Optional[str] = None
    difficulty: int = Field(ge=1, le=10)

class ChallengeCreate(ChallengeBase):
    skill_id: int  
    
class ChallengeOut(ChallengeBase):
    id: int
    skill_id: int

    class Config:
        orm_mode = True
