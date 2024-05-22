#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id', String(60), ForeignKey('places.id'),
        nullable=False, primary_key=True),
    Column(
        'amenity_id', String(60), ForeignKey('amenities.id'),
        nullable=False, primary_key=True)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column("city_id", String(60),
                     ForeignKey("cities.id"), nullable=False)
    user_id = Column("user_id", String(60),
                     ForeignKey("users.id"), nullable=False)
    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024))
    number_rooms = Column("number_rooms", Integer,
                          nullable=False, default=0)
    number_bathrooms = Column("number_bathrooms", Integer,
                              nullable=False, default=0)
    max_guest = Column("max_guest", Integer, nullable=False, default=0)
    price_by_night = Column("price_by_night", Integer,
                            nullable=False, default=0)
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """retrieve reviews associated with place"""
            from models.review import Review
            from models import storage
            reviews_list = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
        

        @property
        def amenities(self):
            """retrieve amenities associated with place"""
            from models.amenity import Amenity
            from models import storage
            amenities_list = []
            all_amenities = storage.all(Amenity).values()
            for amenity in list(all_amenities):
                if amenity.id == self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list
