from sqlalchemy.orm import Session
import models
import schemas
import bcrypt
from fastapi import Response

from datetime import datetime, timedelta
import jwt

# print(jwt)
# print(jwt.__file__,"jwt version")
# print(dir(jwt))


SECRET_KEY = "abcdefghijklmnopqrstuvwxyz"
ALGORITHM = "HS256"



def create_employee(db: Session, employee: schemas.EmployeeCreate):
    #creating  a employee object with user values
    db_employee = models.Employee(**employee.model_dump())
    hashed=bcrypt.hashpw(db_employee.password.encode(),bcrypt.gensalt(rounds=13)).decode("utf-8")
    db_employee.password=hashed
    #adding new employee to existing table
    db.add(db_employee)
    #commiting the changes to the database
    db.commit()
    #refreshing the database to get updated values
    db.refresh(db_employee)
    #returning response to the user
    return db_employee

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None
    db_employee.name = employee.name
    db_employee.department=employee.department 
    db_employee.email=employee.email
    db_employee.location=employee.location

    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None
    db.delete(db_employee)
    db.commit()
    return db_employee



def get_emp_by_dept(db:Session,dept:str):
    print(dept)
    return db.query(models.Employee).filter(
        models.Employee.department==dept
    ).all()


def create_user(user:schemas.UserCreate,db:Session):
    new_user=models.Users(**user.model_dump())
    hashed=bcrypt.hashpw(new_user.password.encode(),bcrypt.gensalt(rounds=12)).decode()
    new_user.password=hashed
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




def login_user(user: schemas.UserLogin, db: Session, response: Response):
    is_exists = db.query(models.Users).filter(
        models.Users.email == user.email
    ).first()

    if not is_exists:
        return {"message": "user not found"}

    valid = bcrypt.checkpw(
        user.password.encode(),
        is_exists.password.encode()
    )

    if not valid:
        return {"message": "invalid password"}

    payload = {
        "name": is_exists.name,
        "email": is_exists.email,
        "is_admin": is_exists.is_admin,
        "is_loggedin":True,
        "exp": datetime.utcnow() + timedelta(seconds=10)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    # Store token in cookie
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True
    )

    return {
        "message": "login successful",
        "access_token": token
    }
