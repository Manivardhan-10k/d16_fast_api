from sqlalchemy.orm import Session
import models
import schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    #creating  a employee object with user values
    db_employee = models.Employee(**employee.model_dump())
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

    