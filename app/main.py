from fastapi import FastAPI
from app.db.session import engine, Base
from app.routes import auth, skill  
from app.models import skills, user, challenges

app = FastAPI()

app.include_router(auth.router)
app.include_router(skill.router)
Base.metadata.create_all(bind=engine)
