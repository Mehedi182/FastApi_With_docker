from fastapi import APIRouter,Depends
from app.session import get_db
from .schemas import *
from .models import Districts
from sqlalchemy.orm import Session



router = APIRouter(
    tags=["crud_router"],
    prefix="/crud_router"
)


@router.get("/", response_model=List[AddressOutSchema])
def get_districts( db: Session = Depends(get_db)):
    data = db.query(Districts).all()
    return data


@router.post("/", response_model=AddressOutSchema)
def create_districts(post_data: AddressCreateSchema,  db: Session = Depends(get_db)):
    new = Districts(**post_data.dict())

    db.add(new)
    db.commit()
    # db.refresh(new)
    return new


