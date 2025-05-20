from config.db import engine, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel

class UserDetail(Base):

   __tablename__ = "userdetails"

   id = Column("id", Integer, primary_key=True)
   dni = Column("dni", Integer)
   firstName = Column("firstname", String)
   lastName = Column("lastname", String)
   type = Column("type", String)
   email = Column("email", String(80), nullable=False, unique=True)


   def __init__(self, dni, firstName, lastName, type, email):
       self.dni = dni
       self.firstName = firstName
       self.lastName = lastName
       self.type = type
       self.email = email


class InputLogin(BaseModel):
    username: str
    password: str

class InputUserDetail(BaseModel):
   dni: int
   firstName: str
   lastName: str
   type: str
   email: str

Base.metadata.create_all(bind=engine)


# creo una clase tipo sessionmaker
Session = sessionmaker(bind=engine)


# instancio un objeto que apunte a cada clase Session
session = Session()