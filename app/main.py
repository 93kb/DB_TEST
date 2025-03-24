from fastapi import FastAPI, HTTPException, APIRouter
from app import models, users
from app.schemas import User, UserCreate

app = FastAPI()
user = APIRouter(prefix='/user', tags=['user'])
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


# ユーザー情報読み込み（read）
@app.get("/users")
def read_user():
    session = models.SessionLocal()
    db_user = session.query(models.User).all()
    return db_user


# ユーザー情報更新（update）
@app.patch("/users")
def update_user():
    session = models.SessionLocal()
    db_user = session.User()
    session.user(users.update().values(
        name = user.name,
        mail = user.mail
    ).where(users.c.id == id))
    
    session.commit()
    session.refresh(db_user)
    return db_user


# ユーザー情報削除（delete）
@app.delete("/users")
def delete_user():
    session = models.SessionLocal()
    db_user = session.User()
    session.delete(db_user)
    session.commit()
    return db_user
