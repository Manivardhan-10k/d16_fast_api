from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

print("api called")




@app.post("/employees", response_model=schemas.EmployeeResponse)
def create(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)






@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def read_one(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def update(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    updated = crud.update_employee(db, employee_id, employee)
    if not updated:
        raise HTTPException(status_code=404, detail="employee not found")
    return updated

@app.delete("/employees/{employee_id}")
def delete(employee_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_employee(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="employee not found")
    return {"message":"employee deleted successfully"}




@app.get("/dept/{dept}")
def get_dept_emp(dept:str,db:Session=Depends(get_db)):
    return crud.get_emp_by_dept(db,dept)