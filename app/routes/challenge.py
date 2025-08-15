from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import User
from app.schemas.challenge import ChallengeCreate, ChallengeOut, ChallengeUpdate
from app.services.challenge_services import update_challenge, delete_challenge, create_challenge, get_all_challenges, get_challenge_by_id
from app.dependencies.roles import require_admin

router = APIRouter(prefix="/challenges", tags=["Challenges"])

@router.post("/", response_model=ChallengeOut, status_code=status.HTTP_201_CREATED)
def create_new_challenge(
    challenge_data: ChallengeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    try:
        return create_challenge(db, challenge_data)
    except HTTPException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=f"Error creating challenge: {e.detail}"
        )
    
@router.get("/{challenge_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_challenge(
    challenge_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    try:
        return get_challenge_by_id(db, challenge_id)
    except HTTPException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=f"Error retrieving challenge: {e.detail}"
        )

@router.get("/{challenge_id}", response_model=list[ChallengeOut])
def update_existing_challenge(
    challenge_id: int,
    challenge_data: ChallengeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    try:
        return update_challenge(db, challenge_id, challenge_data)
    except HTTPException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=f"Error updating challenge: {e.detail}"
        )
    
@router.get("/", response_model=list[ChallengeOut])
def get_all_challenges(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    try:
        return get_all_challenges(db)
    except HTTPException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=f"Error retrieving challenges: {e.detail}"
        )