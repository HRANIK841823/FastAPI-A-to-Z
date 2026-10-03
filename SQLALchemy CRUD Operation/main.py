from sqlalchemy import create_engine, Column, INTEGER, String  # Database-এর engine ও column type import
from sqlalchemy.orm import sessionmaker, declarative_base, Session  # Session ও Model তৈরির প্রয়োজনীয় জিনিস import

from fastapi import FastAPI, Depends,HTTPException  # FastAPI app এবং dependency injection import

app = FastAPI()  # FastAPI-এর application তৈরি করা


DATABASE_URL = "sqlite:///./test.db"  # SQLite database হিসেবে project folder-এ test.db ব্যবহার করা


engine = create_engine(
    DATABASE_URL,  # কোন database-এর সাথে connect হবে সেটা বলা হচ্ছে

    connect_args={"check_same_thread": False}  # SQLite-কে একাধিক thread থেকে ব্যবহার করার অনুমতি দেওয়া
)


SessionLocal = sessionmaker(bind=engine)  # Database session তৈরি করার জন্য একটি Session factory তৈরি করা


Base = declarative_base()  # Database Model তৈরি করার জন্য Base class তৈরি করা


class Todo(Base):  # Todo নামে একটি Database Model তৈরি করছি

    __tablename__ = "todos"  # Database-এ এই Model-এর table-এর নাম হবে todos

    id = Column(INTEGER, primary_key=True, index=True)  # Todo-এর unique ID; Primary Key এবং দ্রুত search-এর জন্য index

    title = Column(String)  # Todo-এর title/name এখানে সংরক্ষণ করা হবে

    completed = Column(String)  # Todo complete হয়েছে কি না সেই information এখানে রাখা হবে


Base.metadata.create_all(bind=engine)  # Todo Model অনুযায়ী database-এ todos table তৈরি করা


def get_db():  # API request-এর জন্য Database Session দেওয়ার function

    db = SessionLocal()  # একটি নতুন Database Session তৈরি করা

    try:
        yield db  # এই database session-টি API endpoint-কে দেওয়া হচ্ছে

    finally:
        db.close()  # API request শেষ হলে database session বন্ধ করা হচ্ছে


#Create Api

@app.post("/todos")
def create_todo(title:str,db :Session=Depends(get_db)):
    todo=Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "Message":"Todo Created",
        "data":todo
    }


#Read all data
@app.get("/todos")
def get_todos(db:Session=Depends(get_db)):
    todos=db.query(Todo).all()
    return{
        "Total":len(todos),
        "data":todos
    }

#Read Specific Data
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="Todo not Found")
    return todo


#update specific Data
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,detail="Todo not Found")

    todo.title=title

    db.commit()
    db.refresh(todo)


    return{
        "message":"Todo Update",
        "data":todo
    }

#Delete Operation
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="Todo not Found")


    db.delete(todo)
    db.commit()

    return{
        "message":"Todo Deleted Successfully",
        "data":todo
    }
    