from rest_api_MTO.producer.dbconfig import *


# ManyToOne
class Customer(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100), nullable=False)
    age = db.Column("age", db.Integer)
    gender = db.Column("gender", db.String(20))
    email = db.Column("email", db.String(100), unique=True)
    active = db.Column("active", db.String(10), default='Y')
    aid = db.Column("aid", db.ForeignKey("address.id"), unique=False, nullable=False)

    def __str__(self):
        return f'{self.__dict__}'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Address(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    city = db.Column("city", db.String(100), nullable=False)
    state = db.Column("state", db.String(100))
    pincode = db.Column("pincode", db.Integer, unique=True)
    active = db.Column("active", db.String(10), default='Y')
    customers = db.relationship("Customer", uselist=True, backref="addresses", lazy=True)

    def __str__(self):
        return f'{self.__dict__}'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


if __name__ == '__main__':
    db.create_all()
    # a1 = Address(id=11, city='Pune1', state='MH', pincode=411041)
    # a2 = Address(id=12, city='Pune2', state='MH', pincode=411042)
    # a3 = Address(id=13, city='Pune3', state='MH', pincode=411043)
    # a4 = Address(id=14, city='Pune4', state='MH', pincode=411044)
    # a5 = Address(id=15, city='Pune5', state='MH', pincode=411045)
    # db.session.add_all([a1,a2,a3,a4,a5])
    # db.session.commit()
    # c1 = Customer(id=101, name='shetty1', age=32, gender='M', email='shetty1@g.in', aid=11)
    # c2 = Customer(id=102, name='shetty2', age=32, gender='M', email='shetty2@g.in', aid=11)
    # c3 = Customer(id=103, name='shetty3', age=32, gender='M', email='shetty3@g.in', aid=12)
    # c4 = Customer(id=104, name='shetty4', age=32, gender='M', email='shetty4@g.in', aid=12)
    # c5 = Customer(id=105, name='shetty5', age=32, gender='M', email='shetty5@g.in', aid=13)
    # db.session.add_all([c3,c4,c5])
    # db.session.commit()
