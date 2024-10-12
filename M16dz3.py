from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{user_age}")
async def user_info(username: str, user_age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {user_age}'
    return f"User {current_index} is registered"

@app.put('/user/{user_id}/{username}/{user_age}')
async def update_id(user_id: int, username: str, user_age: int):
    users[str(user_id)] = f'Имя: {username}, возраст: {user_age}'
    return f'User {user_id} has been updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: int)->str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'