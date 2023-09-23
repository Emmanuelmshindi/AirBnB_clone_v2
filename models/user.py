#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Inherits from class base and basemodel to represent
        a user in the mysql database

    Attributes
    __tablename__(str): the name of the MYSQL table to store users
    email(str):column containing a string and cant be null
    password(str): column containing  a string, can't be null
    first_name: column containing a string, can be null
    first_name: column containing a string, can be null
    places:sqlalchemy relationship The User-Place relationshp
    reviews:sqlalchemy relationnship The User-Review relationship
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Places", backref("user"), cascade("delete"))
    reviews = relationship("Reviews", backref("user"), cascade("delete"))
