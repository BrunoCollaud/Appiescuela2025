from config.db import engine, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel

class Materia(Base):

   __tablename__ = "materias"
   id= Column("id", Integer, primary_key=True)
   nombre=Column("nombre", String)
   estado=Column("estado", String)
   user_id=Column("user_id", Integer, ForeignKey("usuarios.id"))
   career_id=Column("carrer_id", Integer, nullable=True)
   usuario = relationship("User", back_populates="rmateria")

   def __init__(self, nombre, estado, user_id, career_id):
      self.nombre = nombre
      self.estado = estado
      self.user_id = user_id
      self.career_id = career_id


class ImputMateria(BaseModel):
   nombre: str
   estado: str
   user_id: int
   career_id: int


Base.metadata.create_all(bind=engine)


# creo una clase tipo sessionmaker
Session = sessionmaker(bind=engine)


# instancio un objeto que apunte a cada clase Session
session = Session()