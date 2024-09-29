from app import db

class Person(db.Model):
  __tablename__ = 'people'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text())
  age = db.Column(db.Integer)

  def __repr__(self):
    return f'Person named {self.name} age of {self.age}'