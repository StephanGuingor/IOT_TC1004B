from flask_sqlalchemy import BaseQuery
from db import db
from models.base_model import BaseModel
from models.device_ownership import device_client_table
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


class DeviceModel(BaseModel, db.Model):
    __tablename__ = "Device"

    Model = db.Column("Model", db.String(40), primary_key=True)
    PreHeatTime = db.Column("PreHeatTime", db.Integer)
    IdealHumidity = db.Column("IdealHumidity", db.Integer)
    IdealTemperature = db.Column("IdealTemperature", db.Integer)
    Clients = db.relationship(
        "Client", secondary=device_client_table, back_populates="Devices"
    )

    def __init__(self, model, pre_heat_time, ideal_humidity, ideal_temperature):
        self.Model = model
        self.PreHeatTime = pre_heat_time
        self.IdealHumidity = ideal_humidity
        self.IdealTemperature = ideal_temperature

    def json(self):
        return {
            "model": self.Model,
            "pre_heat_time": self.PreHeatTime,
            "ideal_humidity": self.IdealHumidity,
            "ideal_temperature": self.IdealTemperature,
        }

    @classmethod
    def find_by_model(cls, m):

        res = (
            cls.query(DeviceModel)
            .from_statement(text("SELECT * FROM Device where Model=:n"))
            .params(n=m)
            .first()
        )

        db.app.logger.info(f"DEBUG::>> {res}")
        return res
