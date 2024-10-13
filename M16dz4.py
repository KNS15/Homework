
from fastapi import FastAPI, Path, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    user_age: int

users: List[User] = []

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post('/user', response_model=User)
async def add_user(username: str, user_age: int) -> User:
    user_id = len(users) + 1
    user = User(id=user_id, username=username, user_age=user_age)
    users.append(user)
    return user

@app.put('/user/{user_id}', response_model=User)
async def update_user(user_id: int, username: str, user_age: int) -> User:
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    user.username = username
    user.user_age = user_age
    return user

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    users.remove(user)
    return f'Пользователь {user_id} удален'

