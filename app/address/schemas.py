from pydantic import BaseModel
from typing import List, Optional


class AddressOutSchema(BaseModel):
    district: Optional[str]
    code: Optional[str]

    class Config:
        orm_mode = True


class AddressCreateSchema(BaseModel):
    district: str
    code: str

    class Config:
        orm_mode = True


class ListOutSchema(BaseModel):
    upazila_list: List[AddressOutSchema]