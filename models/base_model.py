#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column("id", String(60), nullable=False, primary_key=True)
    created_at = Column("created_at",
                        DateTime(timezone=True),
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column("updated_at",
                        DateTime(timezone=True),
                        nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'created_at':
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        dict = self.__dict__.copy()
        dict.pop("_sa_instance_state", None)
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        import models
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        inst_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                inst_dict[key] = datetime.isoformat(value)
            elif key != '_sa_instance_state':
                inst_dict[key] = value
        inst_dict['__class__'] = self.__class__.__name__
        return inst_dict

    def delete(self):
        """delete current instance object"""
        from models import storage
        storage.delete(self)
