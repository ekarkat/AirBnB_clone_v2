from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
from sqlalchemy.orm import scoped_session
from os import getenv


pla = Place()

print(type(pla.description))