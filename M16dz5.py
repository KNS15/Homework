
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int
    username: str
    user_age: int

users: List[User] = []

@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/users/{user_id}", response_class=HTMLResponse)
async def get_users_list(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')

@app.post("/users/{username}/{user_age}")
async def create_user(username: str, user_age: int):
    user_id = len(users) + 1  # Генерируем ID
    new_user = User(id=user_id, username=username, user_age=user_age)
    users.append(new_user)
    return new_user

@app.put("/users/{user_id}")
async def update_user(user_id: int, age: int):
    if user_id < 1 or user_id > len(users):
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id - 1].user_age = age
    return users[user_id - 1]

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id < 1 or user_id > len(users):
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users.pop(user_id - 1)
    return {"detail": f"User {deleted_user.username} has been deleted"}

