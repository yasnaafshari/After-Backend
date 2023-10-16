from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn
import sqlite3
from user.user import User
from Database.db_queries import *

app = FastAPI(title='After')
database = sqlite3.connect('after.db')
cursor = database.cursor()

cursor.execute(CREATE_TABLE_QUERY)
database.commit()


@app.post("/register")
async def register(email: str, password: str):
    users = cursor.execute(SELECT_USER_BY_EMAIL_QUERY, (email,)).fetchall()
    emails = [user[3] for user in users]
    if email in emails:
        return JSONResponse(content={'success': False, 'message': 'User already exists'})
    else:
        user_data = User(email=email, password=password).dict()
        cursor.execute(INSERT_USER_QUERY, user_data)
        database.commit()
        return JSONResponse(content={'email': email, 'password': password, 'success': True, 'message': 'User created successfully'})


@app.get("/users", response_class=HTMLResponse)
async def get_users():
    cursor.execute(SELECT_ALL_USERS_QUERY,)
    users = cursor.fetchall()
    return JSONResponse(content={"users": users})

if __name__ == "__main__":
    uvicorn.run('after:app', reload=True)
