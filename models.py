from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, Date

Base = declarative_base()


class ToDoList(Base):
    __tablename__ = 'todolist'
    id = Column(Integer, primary_key=True, unique=True)
    task = Column(String)
    date = Column(Date)
    done = Column(Boolean)
