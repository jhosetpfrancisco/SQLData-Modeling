from script3 import app

# Using Interactive Mode Python:
# python -i shellScript3.py

ctx = app.app_context()
ctx.push()

##### For Interactive Mode #####
# from script3 import db, Person
# Person.query.all()
# Person.query.filter_by(name='Amy')
# Person.query
# Person.query.filter_by(name='Amy').all()
# results = Person.query.filter_by(name='Amy').all()
# results[0].id
# person = Person(name='Bob 2')
# db.session.add(person)
# db.session.commit()
# Person.query()
# person1 = Person(name='New Person 1')
# person2 = Person(name='New Person 2')
# db.session.add_all([person1],[person2])
# db.session.commit()
# Person.query()
# exit()