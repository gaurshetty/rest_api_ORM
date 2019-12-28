from rest_api_MTM.producer.dbconfig import *


# ManyToMany
class Customer(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    age = db.Column("age", db.Integer)
    gender = db.Column("gender", db.String(50))
    email = db.Column("email", db.String(100), unique=True)
    active = db.Column("active", db.String(10), default='Y')
    custadr = db.relationship("custAdr", uselist=True, backref="customers", lazy=True)

    def __str__(self):
        return f'{self.__dict__}'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Address(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    city = db.Column("city", db.String(100))
    state = db.Column("state", db.String(50))
    pincode = db.Column("pincode", db.Integer, unique=True)
    active = db.Column("active", db.String(10), default='Y')
    custadr = db.relationship("custAdr", uselist=True, backref="addresses", lazy=True)

    def __str__(self):
        return f'{self.__dict__}'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class custAdr(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    cid = db.Column("cid", db.ForeignKey("customer.id"), unique=False, nullable=False)
    aid = db.Column("aid", db.ForeignKey("address.id"), unique=False, nullable=False)

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
    # c1 = Customer(id=101, name='shetty1', age=32, gender='M', email='shetty1@g.in')
    # c2 = Customer(id=102, name='shetty2', age=32, gender='M', email='shetty2@g.in')
    # c3 = Customer(id=103, name='shetty3', age=32, gender='M', email='shetty3@g.in')
    # c4 = Customer(id=104, name='shetty4', age=32, gender='M', email='shetty4@g.in')
    # c5 = Customer(id=105, name='shetty5', age=32, gender='M', email='shetty5@g.in')
    # db.session.add_all([c1,c2,c3,c4,c5])
    # db.session.commit()
    # ca1 = custAdr(id=1, cid=101, aid=11)
    # ca2 = custAdr(id=2, cid=101, aid=12)
    # ca3 = custAdr(id=3, cid=102, aid=11)
    # ca4 = custAdr(id=4, cid=102, aid=12)
    # ca5 = custAdr(id=5, cid=103, aid=13)
    # db.session.add_all([ca1,ca2,ca3,ca4,ca5])
    # db.session.commit()
