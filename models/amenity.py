#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'


    name = Column('name', String(128), nullable=False, default="")
    place_amenities = relationship("Place", secondary=place_amenity)