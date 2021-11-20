from DB import *
from DeviceOwnership import *

schemaClient = {
    'type': 'object',
    'properties': {
        'Name': {'type': 'varchar'},
    },
    'required': ['Name']
}

class Client(db.Model):
    ClientID= db.Column('ClientID', db.Integer,primary_key=True)
    Name = db.Column('Name', db.String(40), nullable=False)
    devices = db.relationship('device', secondary=DeviceOwnership, lazy='subquery',
        backref=db.backref('clients', lazy=True))


    def __init__(self, name):
        self.Name=name