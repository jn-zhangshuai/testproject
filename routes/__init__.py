from test_a import Flask

from flask_login import LoginManager
import os
from flask_sqlalchemy import SQLAlchemy



MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PWD = os.getenv("MYSQL_PWD", "123456")
MYSQL_DB = os.getenv("MYSQL_DB", "test")

app = Flask(__name__,
            template_folder='../templates',
            static_folder="../assets",
            static_url_path="/assets")


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/test"
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

db = SQLAlchemy(app)

login_manager = LoginManager(app)

import routes.test