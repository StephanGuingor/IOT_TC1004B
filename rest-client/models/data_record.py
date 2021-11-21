from datetime import datetime
from models.base_model import BaseModel
from sqlalchemy import ForeignKeyConstraint
from db import db

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

    def __init__(
        self, client_id, model, gas_concentration, humidity=None, temperature=None
    ):
        self.clientID = client_id
        self.model = model
        self.Humidity = humidity
        self.Temperature = temperature
        self.GasConcentration = gas_concentration
        self.TimeCreated = datetime.utcnow()

    def json(self):
        return {
            "client_id": self.clientID,
            "model": self.model,
            "record_id": self.RecordID,
            "humidity": self.Humidity,
            "temperature": self.Temperature,
            "gas_concentration": self.GasConcentration,
            "time_created": self.TimeCreated.strftime("%m/%d/%Y, %H:%M:%S"),
        }

    @classmethod
    def find_by_id(cls, client_id):
        return cls.query.filter_by(RecordID=client_id).first()
