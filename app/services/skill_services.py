from sqlalchemy.orm import Session
from app.models.skills import Skill
from app.schemas.skill import SkillCreate
from typing import List

def create_skill(db: Session, skill_data: SkillCreate) -> Skill:

    new_skill = Skill(name=skill_data.name, description=skill_data.description)
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill

def get_all_skills(db: Session) -> List[Skill]:
    return db.query(Skill).all()