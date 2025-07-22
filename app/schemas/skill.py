from pydantic import BaseModel

class SkillBase(BaseModel):
    name: str
    description: str | None = None

class SkillCreate(SkillBase):
    pass

class SkillOut(SkillBase):
    id: int

    class Config:
        orm_mode = True