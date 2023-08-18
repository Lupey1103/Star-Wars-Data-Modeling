import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class person(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites = db.relationship('favorites', backref='Person', lazy=True)



class favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    
class planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=True)
    diameter = Column(Integer, nullable=True)
    gravity = Column(Integer, nullable=True)
    population = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    favorites = db.relationship('favorites', backref='Planet', lazy=True)

class character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hairColor = Column(String(250), nullable=True)
    eyeColor = Column(String(250), nullable=True)
    skinColor = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=True)
    birthDate = Column(String(250), nullable=True)
    description = Column(String(250), nullable=True)
    favorites = db.relationship('favorites', backref='Character', lazy=True)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
