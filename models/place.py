#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String
from sqlalchemy import Integer, Float
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))

class Place(BaseModel):
    """ Instantiates a place object and stores it in the Mysql 
    database.
    Class attributes:
    __tablename__(str):place 
    city_id(str(60)): not nullable, foreignkey to cities.id
    user_id(str(60)): not nullable, foreignkey to users.id
    name(str(128)): not null
    description(str(1024)): not null
    number_rooms(int): not null, default=0
    number_bathrooms(int): not null, default=0
    max_guest(int): not null, default=0
    price_by_night(int): not null, default=0
    latitude(float): can be null
    longitude(float): can be null
    amenity_ids(list): An id list of all amenities linked to place
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = Column(list)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []
    overlaps="place_amenities"

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """ Get a list of all linked reviews """
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id = self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """ Get/set linked amenities """
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.place_id = self.id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
