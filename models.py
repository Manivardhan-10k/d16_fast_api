from sqlalchemy import Column, Integer, String,Boolean
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    location= Column(String(50),nullable=False)
    email=Column(String(70),unique=True,nullable=False)
    password=Column(String(30),nullable=False)




class Users(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True,index=True)
    name=Column(String(25),nullable=False)
    email=Column(String(50),unique=True,nullable=False)
    is_active=Column(Boolean,default=True,nullable=False)
    is_admin=Column(Boolean,default=False,nullable=False)
    password=Column(String(300),nullable=False)