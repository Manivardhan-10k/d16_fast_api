from pydantic import BaseModel
class EmployeeCreate(BaseModel):
    name: str
    department:str 
    location:str
    email:str


class EmployeeResponse(EmployeeCreate):
    id: int

    model_config = {
        "from_attributes": True
    }