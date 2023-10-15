from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn
from user.user import User

app = FastAPI(title='After')


@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Welcome to After!</h1>"


users = {
    "user123": "password123"
}


@app.get("/login", response_class=HTMLResponse)
async def login(username: str, password: str):
    if username in users and users[username] == password:
        return JSONResponse(content={"success": True})
    else:
        return JSONResponse(content={"success": False, "message": "Invalid username or password"})


@app.post("/register", response_class=HTMLResponse)
async def register(username: str, password: str):
    if username in users:
        return JSONResponse(content={"success": False, "message": "Username already taken"})
    else:
        username = User(username, password)
        return JSONResponse(content={"success": True})

if __name__ == "__main__":
    uvicorn.run('after:app', reload=True)
