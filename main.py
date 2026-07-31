from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal
from fastapi import Response
from auth import verify_admin
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# print("api called")




@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def read_all(
    db: Session = Depends(get_db),
    user=Depends(verify_admin)
):
    return crud.get_employees(db)








@app.get("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def read_one(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.post("/employees", response_model=schemas.EmployeeResponse)
def create(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

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




@app.post("/register_user")
def user_reg(user:schemas.UserCreate,db:Session=Depends(get_db)):
    return crud.create_user(user,db)



@app.post("/login")
def user_login(response:Response,user:schemas.UserLogin,db:Session=Depends(get_db)):
    return crud.login_user(user,db,response)