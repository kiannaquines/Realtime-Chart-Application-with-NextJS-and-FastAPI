from pydantic import BaseModel
from uuid import UUID,uuid4
from typing import Optional,List
from enum import Enum

class Gender(str, Enum):
    male = "Male"
    female = "Female"

class Roles(str,Enum):
    admin = "Administrator"
    staff = "Staff"
    visitor = "Library Visitor"

class Users(BaseModel):
    id:Optional[UUID] = uuid4()
    first_name:str
    last_name:str
    middle_name:Optional[str]
    age:Optional[int]
    gender: Gender
    role: List[Roles]

class UpdateUser(BaseModel):
    first_name:str
    last_name:str
    middle_name:Optional[str]
    age:int
    gender:Gender
    role:List[Roles]