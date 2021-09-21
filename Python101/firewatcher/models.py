from sqlalchemy import UniqueConstraint
from firewatcher import db


class Cities(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)


class WildFires(db.Model):
    __tablename__ = 'wildfires'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String())
    risk_level = db.Column(db.String())
    type = db.Column(db.String())
    cause = db.Column(db.String())
    locationx = db.Column(db.Float(), nullable=False)
    locationy = db.Column(db.Float(), nullable=False)
    time = db.Column(db.String(), nullable=False)
    district = db.Column(db.String(), nullable=False)
    city = db.Column(db.Integer, db.ForeignKey('cities.id'),
                     nullable=False)
    _table_args__ = (UniqueConstraint('locationx', 'locationy' 'time', "district", "city",  name='_fire_code'),
                     )
