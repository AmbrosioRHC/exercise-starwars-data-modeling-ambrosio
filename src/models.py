import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    
    favorites = relationship("Favorite", back_populates="user")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    
    user = relationship("User", back_populates="favorites")
    person = relationship("Person")
    planet = relationship("Planet")

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(10))
    gender = Column(String(10))
    height = Column(String(10))
    mass = Column(String(10))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    
    favorites = relationship("Favorite", back_populates="person")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(10))
    climate = Column(String(50))
    gravity = Column(String(50))
    terrain = Column(String(50))
    population = Column(String(50))
    
    favorites = relationship("Favorite", back_populates="planet")

render_er(Base, 'diagram.png')
