import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    favorite_character = relationship("Character", backref="user", uselist=False)
    favorite_planet = relationship("Planet", backref="user", uselist=False)
    favorite_vehicles = relationship("Vehicle", backref="user", uselist=False)
    user_id = Column(Integer, ForeignKey("favorites.id"))
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorite_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String(255), nullable=False)
    
class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("favorites.id"))
    name = Column(String(255), nullable=False)
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey("favorites.id"))
    name = Column(String(255), nullable=False)
class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    vehicles_id = Column(Integer, ForeignKey("favorites.id"))
    name = Column(String(255), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
