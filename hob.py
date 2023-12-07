from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session
from os import getenv
from dotenv import load_dotenv
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


load_dotenv()
print(getenv("HBNB_TYPE_STORAGE"))


engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
									"hbnb_dev",
									"hbnb_dev_pwd",
									"localhost",
									"hbnb_dev_db"),
								pool_pre_ping=True)



Session = sessionmaker(bind=engine)

session = Session()




