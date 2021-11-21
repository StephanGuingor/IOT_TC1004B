from DB import *

# schemaDeviceOwnership = {
#     'type': 'object',
#     'properties': {
#         'Model': {'type': 'varchar'},
#         'ClientID': {'type': 'number'},
#         'DeviceOwnerId': {'type': 'number'},
#     },
#     'required': ['Model','Client','DeviceOwnerId']
# }

DeviceOwnership=db.Table('DeviceOwnership', 
db.Column('Model',db.String(40),db.ForeignKey('device.Model'),primary_key=True), 
db.Column('ClientID', db.Integer,db.ForeignKey('client.ClientID'),primary_key=True),
#AQUI PUEDE HABER ERRORES
dataRecord = db.relationship('DataRecord', backref='datarecord', lazy=True))