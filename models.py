from sqlalchemy import Column, Integer, String
from database import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(255))
    email = Column(String(100), unique=True, index=True)
