from config.db import engine, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel


#regionUSER
class User(Base):

   __tablename__ = "usuarios"  # nombre de la tabla en la base de datos


   id = Column("id", Integer, primary_key=True)
   username = Column("username", String)
   password = Column("password", String)
   id_userdetail = Column(Integer, ForeignKey("userdetails.id"))
   userdetail = relationship("UserDetail", backref="user", uselist=False)
   rmateria = relationship("Materia", back_populates="usuario", uselist=True)

   def __init__(self,username,password):
       self.username = username
       self.password = password
#endregion



#region PYDANTIC
class InputUser(BaseModel):
   username: str
   password: str
   email: str
   dni: int
   firstname: str
   lastname: str
   type: str
   



#endregion


#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


# creo una clase tipo sessionmaker
Session = sessionmaker(bind=engine)


# instancio un objeto que apunte a cada clase Session
session = Session()
