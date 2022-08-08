from fastapi import FastAPI
from app.address.routers import router as address_router
app = FastAPI()
app.include_router(address_router)
@app.get('/')
def index():
    return "Hello Word"