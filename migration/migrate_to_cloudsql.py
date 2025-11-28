# migrate_to_cloudsql.py
# Simple migration script that reads from a legacy MySQL and writes to Cloud SQL.
# Replace connection placeholders with real credentials before running.

import mysql.connector
import os

LEGACY_HOST = os.getenv("LEGACY_HOST", "legacy-host")
LEGACY_USER = os.getenv("LEGACY_USER", "root")
LEGACY_PASS = os.getenv("LEGACY_PASS", "root")
LEGACY_DB = os.getenv("LEGACY_DB", "banking")

CLOUD_HOST = os.getenv("CLOUD_HOST", "cloud-sql-ip")
CLOUD_USER = os.getenv("CLOUD_USER", "admin")
CLOUD_PASS = os.getenv("CLOUD_PASS", "password")
CLOUD_DB = os.getenv("CLOUD_DB", "banking")

def get_conn(host, user, password, db):
    return mysql.connector.connect(host=host, user=user, password=password, database=db)

def migrate():
    legacy = get_conn(LEGACY_HOST, LEGACY_USER, LEGACY_PASS, LEGACY_DB)
    cloud = get_conn(CLOUD_HOST, CLOUD_USER, CLOUD_PASS, CLOUD_DB)
    lcur = legacy.cursor()
    ccur = cloud.cursor()

    lcur.execute("SELECT id, name, email, balance, created_at FROM accounts")
    rows = lcur.fetchall()
    for r in rows:
        ccur.execute("INSERT INTO accounts (id, name, email, balance, created_at) VALUES (%s,%s,%s,%s,%s)", r)
    cloud.commit()
    print("Accounts migrated:", len(rows))

if __name__ == '__main__':
    migrate()
