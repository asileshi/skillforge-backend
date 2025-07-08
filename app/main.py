from fastapi import FastAPI
from app.db.session import engine, Base
#from app.routes import auth  # placeholder for future routes (e.g., register/login)
from app.models import user  # this is important to trigger model discovery

app = FastAPI()


@app.get("/ping")
def ping():
    return {"message": "pong"}

# Create tables (only if they don't already exist)
Base.metadata.create_all(bind=engine)
