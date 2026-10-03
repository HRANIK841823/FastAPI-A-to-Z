from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends,HTTPException
from pydantic import BaseModel


# Create FastAPI Application
app = FastAPI()

DATABASE_URL = "sqlite:///./users.db"


# Create engine and connect with database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# Create Session
SessionLocal = sessionmaker(bind=engine)


# Create Base Model
Base = declarative_base()


# ============================================================
# Database Model
# ============================================================

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)


# Create database table
Base.metadata.create_all(bind=engine)


# ============================================================
# Pydantic Schema
# ============================================================

class UserCreate(BaseModel):

    name: str
    email: str
    password: str


# ============================================================
# Database Dependency
# ============================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ============================================================
# Create User API
# ============================================================

@app.post("/user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User Created",
        "data": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
    }

#get user
@app.get("/user")
def get_users(db:Session=Depends(get_db)):
    users=db.query(User).all()
    return{
        "Total":len(users),
        "data":users
    }

#get specific user
@app.get("/user/{user_id}")
def get_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user

#update user
@app.put("/user/{user_id}")
def update_user(user_id:int,person:UserCreate,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not Found")
    user.name=person.name
    user.email=person.email
    user.password=person.password

    db.commit()
    db.refresh(user)

    return {
        "message":"User updated",
        "data":user
    }


#delete user
@app.delete("/user/{user_id}")
def delete_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    

    db.delete(user)
    db.commit()

    return{
        "message":"User deleted Successfully",
        "data":user
    }