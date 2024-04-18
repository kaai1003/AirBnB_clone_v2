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


os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
os.environ['HBNB_MYSQL_HOST'] = 'localhost'
os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'
os.environ['HBNB_TYPE_STORAGE'] = 'db'


state1 = State()
state1.name = "berrechid"

