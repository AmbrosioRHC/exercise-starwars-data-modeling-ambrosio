import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(100), primary_key = True)    
    firstname = Column(String(50), primary_key = False)
    lastname = Column(String(50), primary_key = False)
    email = Column(String(50), primary_key = False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, ForeingKey('user.id'), primary_key = True)
    person_id = Column (Integer, ForeingKey('person.id'))
    planet_id = Column(Integer(100), ForeingKey('planet.id'))
    person_name = Column(String(100), ForeingKey('person.person_name'))
    planet_name = Column(String(100), ForeingKey('planet.planet_name'))


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeingKey('user.id'), primary_key=True)
    person_name = Column(String(250), nullable=False)

class 

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
