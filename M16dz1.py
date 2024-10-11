from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": f"Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user_id(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{user_age}")
async def user_info(username: str, user_age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {user_age}"}

