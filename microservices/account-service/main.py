from fastapi import FastAPI, HTTPException
import os
import mysql.connector

app = FastAPI()

def get_db():
    host = os.getenv("DB_HOST", "127.0.0.1")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    db = os.getenv("DB_NAME", "banking")
    return mysql.connector.connect(host=host, user=user, password=password, database=db)

@app.get("/accounts")
def list_accounts():
    conn = get_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, name, email, balance, created_at FROM accounts")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.get("/accounts/{account_id}")
def get_account(account_id: int):
    conn = get_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, name, email, balance FROM accounts WHERE id=%s", (account_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Account not found")
    return row
