from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.skill import SkillCreate, SkillOut
from app.db import get_db
from app.services.skill_services import create_skill

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.post("/", response_model=SkillOut, status_code=status.HTTP_201_CREATED)
def create_new_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    try:
        skill = create_skill(db, skill)
        return skill
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
