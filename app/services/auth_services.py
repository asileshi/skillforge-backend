from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import UserCreate, Token
from app.utils.security import hash_password, create_access_token

def register_user(db: Session, user_data: UserCreate) -> Token:

    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise ValueError("Username already exists")
    
    hashed_pw = hash_password(user_data.password)

    new_user = User(username=user_data.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(data={"sub": new_user.username})
    
    return Token(access_token=access_token)
