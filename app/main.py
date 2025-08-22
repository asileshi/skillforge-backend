from fastapi import FastAPI
from app.db.session import engine, Base
from app.routes import auth, skill, challenge 
from app.models import skills, user, challenges

app = FastAPI()

app.include_router(auth.router)
app.include_router(skill.router)
app.include_router(challenge.router)
Base.metadata.create_all(bind=engine)
