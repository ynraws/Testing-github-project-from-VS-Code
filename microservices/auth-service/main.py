from fastapi import FastAPI, HTTPException
import os
app = FastAPI()

# Very small demo auth service with static users (for demo only)
USERS = {
    "alice": {"password": "alice123", "id": 1},
    "bob": {"password": "bob123", "id": 2}
}

@app.post("/login")
def login(username: str, password: str):
    user = USERS.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # return a fake token for demo
    return {"access_token": f"token-for-{username}", "user_id": user["id"]}
