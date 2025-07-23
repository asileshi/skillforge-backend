from pydantic import BaseModel
from typing import Optional

class SkillBase(BaseModel):
    name: str
    description: str | None = None

class SkillCreate(SkillBase):
    pass

class SkillOut(SkillBase):
    id: int

    class Config:
        orm_mode = True

class SkillUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None