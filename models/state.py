#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column("name", String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if os.getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def cities(self):
            """return list of cities related to state id"""
            list_cities = []
            dict_cities = models.storage.all(City)
            for city in dict_cities.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
