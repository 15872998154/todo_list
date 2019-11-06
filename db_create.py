from config import SQLALCHEMY_DATABASE_URI
from todo_list import db
import os.path
db.create_all()
