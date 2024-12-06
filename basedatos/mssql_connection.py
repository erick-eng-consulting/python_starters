import os
import json
import pyodbc

server = "den1.mssql8.gear.host"
driver = "{ODBC Driver 18 for SQL Server}"
user = "qesms0yx9f"
password = "OxlDoPQKYJ!"
database = "pydbh8jo6gfmnv"

connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password};TrustServerCertificate=yes"

with pyodbc.connect(connection_string) as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM newtable")
        print(cur.fetchone())