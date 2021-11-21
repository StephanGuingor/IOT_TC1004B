from db import db
from models.base_model import BaseModel
from datetime import datetime
from sqlalchemy import ForeignKeyConstraint

schemaDataRecord = {
    "type": "object",
    "properties": {
        "GasConcentration": {"type": "number"},
        "Humidity": {"type": "number"},
        "Temperature": {"type": "number"},
    },
    "required": ["GasConcentration"],
}


class DataRecordModel(BaseModel, db.Model):
    __tablename__ = "DataRecord"

    RecordID = db.Column("RecordID", db.Integer, primary_key=True)
    Humidity = db.Column("Humidity", db.Integer)
    Temperature = db.Column("Temperature", db.Integer)
    GasConcentration = db.Column("GasConcentration", db.Integer, nullable=False)
    TimeCreated = db.Column(
        "TimeCreated", db.DateTime(timezone=True), default=datetime.utcnow
    )

    model = db.Column("Model", db.String(40))
    clientID = db.Column("ClientID", db.Integer)

    __table_args__ = (
        ForeignKeyConstraint(
            ["Model", "ClientID"],
            ["device_client_table.device_model", "device_client_table.client_id"],
        ),
    )

    def __init__(self, humiduty, temperature, gas_concentration):
        self.Humidity = humiduty
        self.Temperature = temperature
        self.GasConcentration = gas_concentration
        self.TimeCreated = datetime.utcnow
        self.RecordID = ""

    def json(self):
        return {
            "record_id": self.RecordID,
            "humidity": self.Humidity,
            "temperature": self.Temperature,
            "gas_concentration": self.GasConcentration,
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(RecordID=id).first()
