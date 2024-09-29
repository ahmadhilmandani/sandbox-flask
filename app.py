from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Flask

# membuat instance DB menggunakan library SQLAlchemy
db = SQLAlchemy()

def create_app():
  # create flask app
  app = Flask(__name__, template_folder='templates')
  # set database (sqlite) path
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
  
  # init db
  db.init_app(app)

  # register routes 
  from routes import register_routes
  register_routes(app, db)
  
  # migrate the db
  migrate = Migrate(app, db)

  return app