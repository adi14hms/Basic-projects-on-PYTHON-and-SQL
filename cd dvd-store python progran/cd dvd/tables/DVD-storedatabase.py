import mysql.connector as sql
conn = sql.connect(
  host="localhost",
  user="root",
  password="1234"
)

if conn.is_connected():
    print("sucessfully connected")

conn.cursor().execute("CREATE DATABASE DVD")
print("Database Successfully Created")
