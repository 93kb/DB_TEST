import sqlite3
from fastapi import FastAPI
from google import genai
from pydantic import BaseModel

dbname = 'APItest.db'
app = FastAPI()

conn=sqlite3.connect(dbname)
c = conn.cursor()

# executeメソッドでSQL文を実行する
create_table = '''create table toukeilab (id value,name verchar)'''
c.execute(create_table)