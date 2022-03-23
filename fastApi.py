from importlib.resources import path
from typing import Optional
from unittest.mock import patch
from fastapi import FastAPI,Path

app = FastAPI()

students = {
    1:{
        'name':'mohamed',
        'age':'22',
        'address':'mansoura'
    },2:{
        'name':'ebrahim',
        'age':'22',
        'address':'samanoud'
    },3:{
        'name':'nader',
        'age':'22',
        'address':'aga'
    },4:{
        'name':'ramzy',
        'age':'22',
        'address':'Manzala'
    },5:{
        'name':'yasmin',
        'age':'22',
        'address':'alex'
    },6:{
        'name':'eslam',
        'age':'22',
        'address':'mansoura'
    },7:{
        'name':'nabil',
        'age':'22',
        'address':'manzala'
    },8:{
        'name':'hajar',
        'age':'23',
        'address':'manzala'
    }

     
}

# get information
@app.get("/")
def index():
    # fastapi use json data so we use python dictionary
    return{"name":"mohamed khaled"}

# return student when i enter id 
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None,description = "The id of the student that u want to view",gt=0 )):
    return students[student_id]

# get students by name
@app.get("/get-by-name")
def get_student(*,name:Optional [str] = None , test:int ):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not Found"}
# i am stopping at 37min