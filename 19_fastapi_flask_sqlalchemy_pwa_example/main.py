from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from a2wsgi import WSGIMiddleware

from api import router as api_router
from web import flask_app
from database import Base, engine
from models import User

app = FastAPI(title="Steven API")

Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api")
app.mount("/web", WSGIMiddleware(flask_app))

@app.get("/", response_class=RedirectResponse)
async def redirect_to_web():
    return "/web/"
