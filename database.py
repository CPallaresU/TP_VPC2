from google.cloud.sql.connector import Connector
import sqlalchemy
import sys
import os

#os.system("gcloud auth application-default login")

a_='aimbot-363723:'
b_='us-central1:'
c_='aimbotdb'

INSTANCE_CONNECTION_NAME = f'{a_,b_,c_}' # i.e demo-project:us-central1:demo-instance
#print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")
DB_USER = "postgres"
DB_PASS = "ma31a19pu"
DB_NAME = "aimdbx"

# initialize Connector object
connector = Connector()

# function to return the database connection object
def getconn():

    conn = connector.connect(
        'aimbot-363723:us-central1:aimbotdb',
        "pg8000",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

"""
# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn
)
# connect to connection pool
with pool.connect() as db_conn:
  # create ratings table in our movies database
  db_conn.execute(
      "CREATE TABLE IF NOT EXISTS puntosxy ( x INT ,y INT );"
  )
  # insert data into our ratings table
  insert_stmt = sqlalchemy.text(
      "INSERT INTO puntosxy (x, y) VALUES (:x, :y)")

  # insert entries into table
  
  db_conn.execute(insert_stmt, x=-100, y=-10)
"""
#connector.close()
