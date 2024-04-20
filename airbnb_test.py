#!/usr/bin/python3

import sys
import re
import os
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


state3 = State()
state3.name = "test2333"
storage.new(state3)
storage.save()
all_objcs = storage.all()
for obj_id in all_objcs.keys():
    obj = all_objcs[obj_id]
    print(obj)
