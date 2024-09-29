# list of routes/api endpoint
from model.user import User

def register_routes(app, db):
  @app.route('/')
  def index():
    user = User.query.all()
    return str(user)