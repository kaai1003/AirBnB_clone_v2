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


city1 = City()
city1.state_id = "e7fbe122-7a10-42cb-b100-c60236fa700a"
city1.name = "test1"
storage.new(city1)
storage.save()
