from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.skill import SkillCreate, SkillOut, SkillUpdate
from app.db import get_db
from app.services.skill_services import create_skill, get_skill_by_id, get_all_skills, update_skill, delete_skill
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.post("/", response_model=SkillOut, status_code=status.HTTP_201_CREATED)
def create_new_skill(skill: SkillCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        skill = create_skill(db, skill)
        return skill
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=list[SkillOut])
def read_all_skills(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    skills = get_all_skills(db)
    return skills
    
@router.get("/{skill_id}", response_model=SkillOut)
def read_skill(skill_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    skill = get_skill_by_id(skill_id, db)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

@router.put("/{skill_id}", response_model=SkillOut)
def update_existing_skill(skill_id: int, skill_data: SkillUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_skill(db, skill_id, skill_data)

@router.delete("/{skill_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_skill(skill_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    delete_skill(db, skill_id)
