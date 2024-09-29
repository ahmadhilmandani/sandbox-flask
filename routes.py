from model.person import Person

# from app import app, db
def register_routes(app, db):
  
  @app.route('/get-person')
  def index():
    people = Person.query.all()
    return str(people)

