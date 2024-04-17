#!/usr/bin/python3

import sys
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



state1 = State()
state1.name = "berrechid"
print(storage.all())
storage.new(state1)
storage.save()
print(storage.all())

