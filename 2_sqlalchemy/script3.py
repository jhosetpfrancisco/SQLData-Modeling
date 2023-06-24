from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

# We need to use app_context to do something out from route
with app.app_context():
    db.create_all()
    # To add new Person on our table
    # person = Person(name='Amy')
    # db.session.add(person)
    # db.session.commit()


@app.route("/")
def index():
    person = Person.query.first()
    return "Hello " + person.name
