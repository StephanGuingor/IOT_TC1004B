from db import db

# schemaDeviceOwnership = {
#     'type': 'object',
#     'properties': {
#         'Model': {'type': 'varchar'},
#         'ClientID': {'type': 'number'},
#         'DeviceOwnerId': {'type': 'number'},
#     },
#     'required': ['Model','Client','DeviceOwnerId']
# }


device_client_table = db.Table(
    "device_client_table",
    db.Column(
        "client_id",
        db.Integer,
        db.ForeignKey("Client.ClientID"),
        primary_key=True,
        nullable=False,
    ),
    db.Column(
        "device_model",
        db.String(40),
        db.ForeignKey("Device.Model"),
        primary_key=True,
        nullable=False,
    ),
)

# class DeviceOwnershipModel(db.Model):
#     __tablename__ = "DeviceOwnership"
#     ClientID = db.Column(db.Integer, db.ForeignKey("Client.ClientID"), primary_key=True)
#     Model = db.Column(db.Integer, db.ForeignKey("Device.Model"), primary_key=True)
#     Devices = db.relationship("Device", secondary="DeviceOwnership")
#     Clients = db.relationship("Client", secondary="DeviceOwnership")
