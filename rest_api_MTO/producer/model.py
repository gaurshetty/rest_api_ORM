from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/pco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# one_to_one
class Customer(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    age = db.Column("age", db.Integer)
    gender = db.Column("gender", db.String(50))
    email = db.Column("email", db.String(100), unique=True)
    active = db.Column("active", db.String(10), default='Y')
    addresses = db.relationship("Address", uselist=False, backref="customers", lazy=False)

    def __str__(self):
        return f'{self.__dict__}'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Address(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    city = db.Column("city", db.String(100))
    state = db.Column("state", db.String(100))
    pincode = db.Column("pincode", db.Integer, unique=True)
    active = db.Column("active", db.String(10), default='Y')
    cid = db.Column("cid", db.ForeignKey("customer.id"), unique=True, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
