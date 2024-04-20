#!/usr/bin/python3
"""This module defines a class to manage DB storage"""
import json
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os


class DBStorage:
    """DB storage class definition"""
    __engine = None
    __session = None
    classes = (BaseModel, State, City, Place, Review, Amenity, User)

    def __init__(self):
        """engine DB initialisation"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(user,
                                             pwd,
                                             host,
                                             db), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """load objects from DB
        Args
            cls (class): class name to be loaded
        """
        objs_dict = {}
        if cls is not None:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = obj.__class__.__name__ + '.' + obj.id
                objs_dict[key] = obj
        else:
            for value in self.classes:
                objects = self.__session.query(value).all()
                for obj in objects:
                    key = type.__class__.__name__ + '.' + obj.id
                    objs_dict[key] = obj
        return objs_dict

    def new(self, obj):
        """add obj to DB
        Args
            obj: object to add
        """
        self.__session.add(obj)

    def save(self):
        """commit changes to DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from DB
        Args
            obj: object to delete
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables on DB"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
