import sqlite3
from fastapi import FastAPI, HTTPException
from google import genai
from app import models

dbFile = 'test.db'
# 1.データベースに接続
con = sqlite3.connect(dbFile)

# 2.sqliteを操作するカーソルオブジェクトを作成
cur = con.cursor()

app = FastAPI()

# Todoを登録　参考https://qiita.com/mtitg/items/47770e9a562dd150631d
@app.post("/todos/")
async def create_todo(todo_in: TodoIn,  db: Session = Depends(get_db)):
    todo = Todo(title=todo_in.title, done=False)
    db.add(todo)
    db.commit()
    todo = get_todo(db, todo.id)
    return todo

# Todoを更新
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_in: TodoIn, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    todo.title = todo_in.title
    todo.done = todo_in.done
    db.commit()
    todo = get_todo(db, todo_id)
    return todo


"""
# ユーザー登録（create）
@app.post("/users", response_model=User)
def create_user(request: UserCreate):
    db_user = models.User(email=request.email, name=request.name)
    session = models.SessionLocal()
    try:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return db_user

    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

"""
