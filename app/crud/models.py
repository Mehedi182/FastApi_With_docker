from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from app.db.base import Base


class Districts(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    district = Column(String)
    code = Column(String)

    @declared_attr
    def __tablename__(cls) -> str:
        return 'districts'
