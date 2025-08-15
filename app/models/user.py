from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from app.db.session import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    create_at = Column(DateTime, default=datetime.utcnow)

    skills = relationship("Skill", back_populates="owner", cascade="all, delete-orphan")