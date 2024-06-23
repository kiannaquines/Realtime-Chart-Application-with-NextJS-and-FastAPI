from fastapi import FastAPI, HTTPException
from typing import List
from models.models import Users,Roles,Gender,UpdateUser
from uuid import UUID,UUID

app = FastAPI()

usersDB: List[Users] = [
    Users(
        id=UUID("b43d94ed-5428-467d-aaf3-d3dc1eb4af6f"),
        first_name="Kian",
        last_name="Naquines",
        middle_name="Geraldez",
        age=21,
        gender=Gender.male,
        role=[Roles.admin]
    ),
    Users(
        id=UUID("b301f93f-a812-4115-9076-128e27fcfba6"),
        first_name="James",
        last_name="Naquines",
        middle_name="Geraldez",
        age=22,
        gender=Gender.male,
        role=[Roles.staff]
    ),
    Users(
        id=UUID("6dbc2b08-5a81-44c1-b4c6-8ca6c9e19ba4"),
        first_name="Larry",
        last_name="Naquines",
        middle_name="Geraldez",
        age=25,
        gender=Gender.male,
        role=[Roles.visitor]
    ),
    Users(
        id=UUID("95f7837d-c72c-4048-97b4-ea4b226a56d1"),
        first_name="Anna",
        last_name="Dayaday",
        middle_name="Naquines",
        age=45,
        gender=Gender.female,
        role=[Roles.visitor]
    )
]

@app.get("/")
async def index():
    return {"message":"Server is running...."}

@app.get("/api/v1/users")
async def users_list():
    return usersDB

@app.post("/api/v1/users")
async def add_user(user: Users):
    usersDB.append(user)
    return {"id":user.id}

@app.delete("/api/v1/users/delete/{user_id}")
async def delete_user(user_id: UUID):
    for user in usersDB:
        if user.id == user_id:
            usersDB.remove(user)

            raise HTTPException(
                status_code=200,
                detail=f"You have successfully remove {user_id}`"
            )
        
    raise HTTPException(
        status_code=404,
        detail=f"User with id {user_id} was not found.."
    )

@app.put("/api/v1/users/edit/{user_id}")
async def edit_user(update_user: UpdateUser, user_id: UUID):
    for user in usersDB:
        if user.id == user_id:
            user.first_name = update_user.first_name
            user.last_name = update_user.last_name
            user.middle_name = update_user.middle_name
            user.age = update_user.age
            user.gender = update_user.gender
            user.role = update_user.role

            raise HTTPException(
                status_code=200,
                detail=f"You have successfully updated {update_user.first_name}'s account"
            )
        
    raise HTTPException(
        status_code=404,
        detail=f"User with id {user_id} was not found.."
    )