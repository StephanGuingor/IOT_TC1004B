from db import db
from models.base_model import BaseModel
from sqlalchemy.sql import text

schemaDevice = {
    "type": "object",
    "properties": {
        "Model": {"type": "varchar"},
        "PreHeatTime": {"type": "number"},
        "IdealHumidity": {"type": "number"},
        "IdealTemperature": {"type": "number"},
    },
    "required": ["Model"],
}


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


# class Link(BaseModel, db.Model):
#     __tablename__ = "link"
#     client_id = (
#         db.Column(
#             db.Integer,
#             db.ForeignKey("Client.ClientID"),
#             primary_key=True,
#             nullable=False,
#         ),
#     )
#     device_model = (
#         db.Column(
#             db.Integer,
#             db.ForeignKey("Client.ClientID"),
#             primary_key=True,
#             nullable=False,
#         ),
#     )


class DeviceModel(BaseModel, db.Model):
    __tablename__ = "Device"

    Model = db.Column("Model", db.String(40), primary_key=True)
    PreHeatTime = db.Column("PreHeatTime", db.Integer)
    IdealHumidity = db.Column("IdealHumidity", db.Integer)
    IdealTemperature = db.Column("IdealTemperature", db.Integer)
    Clients = db.relationship("ClientModel", secondary="device_client_table")

    def __init__(self, model, pre_heat_time, ideal_humidity, ideal_temperature):
        self.Model = model
        self.PreHeatTime = pre_heat_time
        self.IdealHumidity = ideal_humidity
        self.IdealTemperature = ideal_temperature

    def json(self, local=True):
        m = {
            "model": self.Model,
            "pre_heat_time": self.PreHeatTime,
            "ideal_humidity": self.IdealHumidity,
            "ideal_temperature": self.IdealTemperature,
        }

        if local:
            m["clients"] = [c.json(False) for c in self.Clients]

        return m

    @classmethod
    def find_by_model(cls, m) -> "DeviceModel":
        return cls.query.filter_by(Model=m).first()
