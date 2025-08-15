from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.challenges import Challenge
from app.models.skills import Skill
from app.models.user import User
from app.schemas.challenge import ChallengeCreate, ChallengeUpdate
from typing import List

def create_challenge(db: Session, challenge_data: ChallengeCreate, current_user: User) -> Challenge:
    skill = db.query(Skill).filter(
        Skill.id == challenge_data.skill_id,
        Skill.owner_id == current_user.id
        ).first()
    
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found or not owned by user")
    