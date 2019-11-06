from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SECRET_KEY"] = "12345678"

app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from todo_list import views, models # 导入视图函数 




