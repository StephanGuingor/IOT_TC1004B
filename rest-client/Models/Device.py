from DB import *
from DeviceOwnership import *

schemaDevice = {
    'type': 'object',
    'properties': {
        'Model': {'type': 'varchar'},
        'PreHeatTime': {'type': 'number'},
        'IdealHumidity': {'type': 'number'},
        'IdealTemperature': {'type': 'number'},
    },
    'required': ['Model']
}

class Device(db.Model):
    Model= db.Column('Model', db.String(40),primary_key=True)
    PreHeatTime = db.Column('PreHeatTime', db.Integer)
    IdealHumidity = db.Column('IdealHumidity', db.Integer)
    IdealTemperature = db.Column('IdealTemperature', db.Integer)
    clients = db.relationship('client', secondary=DeviceOwnership, lazy='subquery',
        backref=db.backref('devices', lazy=True))

    def __init__(self, model, pre_heat_time, ideal_humidity, ideal_temperature):
        self.Model=model
        self.PreHeatTime=pre_heat_time
        self.IdealHumidity=ideal_humidity
        self.IdealTemperature=ideal_temperature
