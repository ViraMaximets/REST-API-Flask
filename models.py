from __init__ import *
import enum


class Admin(Base):
    __tablename__ = 'admin'

    adminId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Brand(Base):
    __tablename__ = 'brand'

    brandId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)


class Car(Base):
    __tablename__ = 'car'

    carId = db.Column(db.Integer, primary_key=True, autoincrement=True)

    brand_id = db.Column(db.Integer, db.ForeignKey(Brand.brandId))
    brand = db.relationship(Brand, backref=db.backref('brand'))

    model = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))


class User(Base):
    __tablename__ = 'user'

    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(40), nullable=False)


class RentStatus(enum.Enum):
    REQUEST = 'REQUEST'
    APPROVED = 'APPROVED'
    DENIED = 'DENIED'


class Rent(Base):
    __tablename__ = 'rent'

    rentId = db.Column(db.Integer, primary_key=True, autoincrement=True)

    owner_id = db.Column(db.Integer, db.ForeignKey(User.userId))
    owner = db.relationship(User, backref=db.backref('owner'))

    car_id = db.Column(db.Integer, db.ForeignKey(Car.carId))
    car = db.relationship(Car, backref=db.backref('car'))

    startT = db.Column(db.Date, nullable=False)
    endT = db.Column(db.Date, nullable=False)

    status = db.Column(db.String(10), default=RentStatus.REQUEST.value)


