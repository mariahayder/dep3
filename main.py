
from typing import Dict

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel



app = FastAPI()
app.N=-1
app.patients=[]

@app.get("/method")
def root():
    return {"method": "GET"}

class PatientRq(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id:int
    patient: Dict
class HelloResp(BaseModel):
    msg: str


@app.get("/hello/{name}", response_model=HelloResp)
def read_item(name: str):
    return HelloResp(msg=f"Hello {name}")


class GiveMeSomethingRq(BaseModel):
    first_key: str


class GiveMeSomethingResp(BaseModel):
    received: Dict
    constant_data: str = "POST"



@app.get("/patient/{pk}", response_model=PatientRq)
def pk(pk:int):
    #pK=int(pk)
    print(pk)
    if pk < len(app.patients):
        current=app.patients[pk]
        print(current.patient['name'])
        return PatientRq(name=current.patient['name'], surename=current.patient['surename'])
    else:    
        raise HTTPException(status_code=404)
        


"""
@app.post("/method", response_model=GiveMeSomethingResp)
def receive_something(rq: GiveMeSomethingRq):
    return GiveMeSomethingResp(received=rq.dict())
    """
#class PostRq(BaseModel):
    #first_key: str
#zad2
class PostResp(BaseModel):
    method: str

@app.delete("/method", response_model=PostResp)
def delete_something():
    return PostResp(method="DELETE")     

@app.post("/method", response_model=PostResp)
def post_something():
    return PostResp(method="POST")   

@app.put("/method", response_model=PostResp)
def put_something():
    return PostResp(method="PUT")      
#patient-zad3

    
   
@app.post("/patient", response_model=PatientResp)
def create_patient(rq: PatientRq):
    app.N+=1
    N=app.N
    app.patients.append(PatientResp(id=N, patient=rq.dict()))
    return PatientResp(id=N, patient=rq.dict())
