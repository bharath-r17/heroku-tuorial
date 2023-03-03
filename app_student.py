from typing import Optional  
from fastapi import FastAPI  
from pydantic import BaseModel  
   
class Student(BaseModel):  
    id : int  
    name: str  
    address: Optional[str] = None  
    branch: str  
   
app = FastAPI()  

 # Define the default route 
@app.get("/")
def root():
    return {"message": "Welcome to Student Application Form"}
  
@app.post("/students/")  
def create_student(student: Student):  
    return student

# uvicorn app_student:app --reload