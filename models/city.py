#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ Represents a city for the MySQL database
        Inherits from sqlalchemy base and links to mysql table 
        cities
    """
    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
