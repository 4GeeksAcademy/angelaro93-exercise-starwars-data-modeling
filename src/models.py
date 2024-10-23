import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
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
    date = Column(Date(), unique=True, nullable=False)

    favs = relationship("Fav", back_populates="user")


class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)  
    description = Column(String(200), nullable=True)

    favs = relationship("Fav", back_populates="planet")


class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)  
    description = Column(String(200), nullable=True) 

    favs = relationship("Fav", back_populates="character")


class Fav(Base):
    __tablename__ = 'fav'
    
    id = Column(Integer, primary_key=True)  # Primary key para la tabla de favoritos
    id_user = Column(Integer, ForeignKey('user.id'))
    id_character = Column(Integer, ForeignKey('character.id'))
    id_planet = Column(Integer, ForeignKey('planet.id'))

    user = relationship("User", back_populates="favs")
    character = relationship("Character", back_populates="favs")
    planet = relationship("Planet", back_populates="favs")









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

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
