from fastapi import FastAPI
import os
import mysql.connector
from google.cloud import pubsub_v1

app = FastAPI()

PROJECT = os.getenv("PROJECT_ID", "")
TOPIC = os.getenv("PAYMENTS_TOPIC", "payments-topic")

def publish_payment_event(payment):
    try:
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(PROJECT, TOPIC)
        data = str(payment).encode("utf-8")
        publisher.publish(topic_path, data=data)
    except Exception as e:
        print("PubSub publish failed:", e)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "banking")
    )

@app.post("/payments")
def create_payment(account_id: int, amount: float):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO payments (account_id, amount, status) VALUES (%s,%s,%s)", (account_id, amount, "PENDING"))
    conn.commit()
    pid = cur.lastrowid
    cur.close()
    conn.close()
    publish_payment_event({"payment_id": pid, "account_id": account_id, "amount": amount})
    return {"payment_id": pid, "status": "PENDING"}
