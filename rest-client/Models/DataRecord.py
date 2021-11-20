from DB import *
from DeviceOwnership import *
from datetime import datetime
from sqlalchemy import (create_engine, Column, String, ForeignKey,
                        ForeignKeyConstraint)

schemaDataRecord = {
    'type': 'object',
    'properties': {
        'GasConcentration': {'type': 'number'},
        'Humidity': {'type': 'number'},
        'Temperature': {'type': 'number'},
    },
    'required': ['GasConcentration']
}

class DataRecord(db.Model):
    RecordID= db.Column('RecordID', db.Integer,primary_key=True)
    Humidity = db.Column('Humidity', db.Integer)
    Temperature = db.Column('Temperature', db.Integer)
    GasConcentration = db.Column('GasConcentration', db.Integer, nullable=False)
    TimeCreated = db.Column('TimeCreated', db.DateTime(timezone=True), default=datetime.utcnow)
    

    DeviceOwnerID=db.Column(db.Integer,db.ForeignKey('DeviceOwnership.slug'), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(
            ['Model', 'ClientID'],
            ['DeviceOwnerShip.Model', 'DeviceOwnerShip.ClientID'],
        ),
    )

    def __init__(self, Humidity, Temperature, GasConcentration):
        self.Humidity=Humidity
        self.Temperature=Temperature
        self.GasConcentration=GasConcentration
