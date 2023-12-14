import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

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


class User(Base): #parent
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    Username = Column(String(10), nullable= False, unique=True)
    password = Column(String (12), nullable= False)
    favorite_list = relationship("Favorite_list", back_populates="user")

class Favorite_list(Base): #child
    __tablename__ = 'favorite_list'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="favorite_list")




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
