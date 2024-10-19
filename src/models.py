import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er



Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)  
    address = Column(String(50), nullable=False) 
    phone = Column(String(50), nullable=False) 

    likes = relationship("Like", back_populates="user")


class Planet(Base):
     __tablename__ = 'planet'

     id = Column(Integer, primary_key=True)
     name = Column(String(50), nullable=False, unique=True)  
     description = Column(String(200), nullable=True)

     likes = relationship("Like", back_populates="planets")
     


class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)  
    description = Column(String(200), nullable=True) 

    likes = relationship("Like", back_populates="character")

    

class Like(Base):
     __tablename__ = 'like'
    
     id_user = Column(Integer, ForeignKey('user.id'), primary_key=True)
     id_character = Column(Integer, ForeignKey('character.id'), primary_key=True)
     id_planet = Column(Integer, ForeignKey('planet.id'), primary_key=True)

     user = relationship("User", back_populates="likes")
     character = relationship("character", back_populates="likes")
     planets = relationship("Planets", back_populates="likes")
    

    







# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')
