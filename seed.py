from app import db
from model.person import Person

person1 = Person(name="John Doe", age=30)
person2 = Person(name="Jane Smith", age=25)
person3 = Person(name="Bob Johnson", age=35)

db.session.add(person1)
db.session.add(person2)
db.session.add(person3)

db.session.commit()