from sqlalchemy.orm import Session
from app.models.skills import Skill
from app.schemas.skill import SkillCreate, SkillUpdate
from typing import List

def create_skill(db: Session, skill_data: SkillCreate) -> Skill:

    new_skill = Skill(name=skill_data.name, description=skill_data.description)
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill

def get_all_skills(db: Session) -> List[Skill]:
    return db.query(Skill).all()

def get_skill_by_id(skill_id: int, db: Session) ->Skill:
    return db.query(Skill).filter(Skill.id == skill_id).first()

def update_skill(db: Session, skill_id: int, skill_data: SkillUpdate) -> Skill:
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")  
    if skill_data.name is not None:
        skill.name = skill_data.name
    if skill_data.description is not None:
        skill.description = skill_data.description
    db.commit()
    db.refresh(skill)
    return skill