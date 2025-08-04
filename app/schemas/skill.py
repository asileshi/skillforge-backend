from pydantic import BaseModel
from typing import Optional
from app.schemas.auth import UserOut

class SkillBase(BaseModel):
    name: str
    description: str | None = None

class SkillCreate(SkillBase):
    pass

class SkillOut(SkillBase):
    id: int
    owner: UserOut

    class Config:
        orm_mode = True

class SkillUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None