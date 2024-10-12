from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": f"Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user_id(user_id: int =Path(ge=0, le=100, description="Enter user id", example="26")) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{user_age}")
async def user_info(username: Annotated[str,Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                    user_age: Annotated[int,Path(min_length=18, max_length=120, description="Enter age", example="24")]) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {user_age}"}

