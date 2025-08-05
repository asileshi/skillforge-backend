from sqlalchemy.orm import Session
from app.models.skills import Skill
from app.models.user import User
from fastapi import HTTPException
from app.schemas.skill import SkillCreate, SkillUpdate
from typing import List

def create_skill(db: Session, skill_data: SkillCreate, current_user: User) -> Skill:

    new_skill = Skill(
        name=skill_data.name, 
        description=skill_data.description,
        owner_id=current_user.id
    )
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill

def get_skills_for_user(db: Session, current_user: User) -> List[Skill]:
    return db.query(Skill).filter(Skill.owner_id == current_user.id).all()

def get_skill_by_id(skill_id: int, db: Session, current_user: User) -> Skill:
    return db.query(Skill).filter(Skill.id == skill_id, Skill.owner_id == current_user.id).first()

def update_skill(db: Session, skill_id: int, skill_data: SkillUpdate, current_user: User) -> Skill:
    skill = db.query(Skill).filter(Skill.id == skill_id, Skill.owner_id == current_user.id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")  
    if skill_data.name is not None:
        skill.name = skill_data.name
    if skill_data.description is not None:
        skill.description = skill_data.description
    db.commit()
    db.refresh(skill)
    return skill

def remove_skill(db: Session, skill_id: int, current_user: User) -> None:
    skill = db.query(Skill).filter(Skill.id == skill_id, Skill.owner_id == current_user.id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    db.delete(skill)
    db.commit()
