from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.challenges import Challenge
from app.models.skills import Skill
from app.models.user import User
from app.schemas.challenge import ChallengeCreate, ChallengeUpdate
from typing import List

def create_challenge(db: Session, challenge_data: ChallengeCreate) -> Challenge:
    skill = db.query(Skill).filter(Skill.id == challenge_data.skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    challenge = Challenge(
        title=challenge_data.title,
        description=challenge_data.description,
        difficulty=challenge_data.difficulty,
        skill_id=challenge_data.skill_id
    )
    db.add(challenge)
    db.commit()
    db.refresh(challenge)
    return challenge

def get_all_challenges(db: Session) -> List[Challenge]:
    challenges = db.query(Challenge).all()
    return challenges

def get_challenge_by_id(db: Session, challenge_id: int) -> Challenge:
    challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return challenge

def update_challenge(db: Session, challenge_id: int, challenge_data: ChallengeUpdate) -> Challenge:
    challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    
    for key, value in challenge_data.dict(exclude_unset=True).items():
        setattr(challenge, key, value)
    db.commit()
    db.refresh(challenge)
    return challenge

def delete_challenge(db: Session, challenge_id: int) -> None:
    challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    db.delete(challenge)
    db.commit()
    return None

