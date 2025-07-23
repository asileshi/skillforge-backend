from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.skill import SkillCreate, SkillOut
from app.db import get_db
from app.services.skill_services import create_skill, get_skill_by_id, get_all_skills

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.post("/", response_model=SkillOut, status_code=status.HTTP_201_CREATED)
def create_new_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    try:
        skill = create_skill(db, skill)
        return skill
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=list[SkillOut])
def read_all_skills(db: Session = Depends(get_db)):
    skills = get_all_skills(db)
    return skills
    
@router.get("/{skill_id}", response_model=SkillOut)
def read_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = get_skill_by_id(skill_id, db)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill
