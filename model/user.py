# user class model
from app import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.Text)
  role = db.Column(db.Text)

  def __repr__(self):
        return f'user {self.name}'