import os
import json
import psycopg

server = "esalas-training.claigao4w9t7.us-east-1.rds.amazonaws.com"

connection_string = f"postgresql://postgres:JRLCoUxO935jz0NKUTps@{server}"

with psycopg.connect(connection_string) as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM newtable")
        print(cur.fetchone())