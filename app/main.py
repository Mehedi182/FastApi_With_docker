from fastapi import FastAPI
from app.crud.routers import router as crud_router
app = FastAPI()
app.include_router(crud_router)
@app.get('/')
def index():
    return "Hello Word"