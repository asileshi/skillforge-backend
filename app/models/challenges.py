from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.session import Base

class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    difficulty = Column(Integer, nullable=True, default=1) 

    skill_id = Column(Integer, ForeignKey("skills.id"))

    skill = relationship("Skill", back_populates="challenges")
