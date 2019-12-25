from rest_api_MTO.producer.dbconfig import *


# ManyToOne
class Customer(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100), nullable=False)
    age = db.Column("age", db.Integer)
    gender = db.Column("gender", db.String(20))
    email = db.Column("email", db.String(100), unique=True)
    active = db.Column("active", db.String(10), default='Y')
    aid = db.Column("aid", db.ForeignKey("Address.id"), unique=False, nullable=False)

    def __str__(self):
        return str(self)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Address(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    city = db.Column("city", db.String(100), nullable=False)
    State = db.Column("State", db.String(100))
    pincode = db.Column("pincode", db.Integer, unique=True)
    active = db.Column("active", db.String(10), default='Y')
    customers = db.relationship("Customer", uselist=True, backref="addresses", lazy=True)

    def __str__(self):
        return str(self)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}