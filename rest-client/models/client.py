from db import db
from models.base_model import BaseModel
from models.device_ownership import device_client_table

schemaClient = {
    "type": "object",
    "properties": {
        "Name": {"type": "varchar"},
    },
    "required": ["Name"],
}


class ClientModel(BaseModel, db.Model):
    __tablename__ = "Client"

    ClientID = db.Column("ClientID", db.Integer, primary_key=True)
    Name = db.Column("Name", db.String(40), nullable=False)
    Devices = db.relationship(
        "Device", secondary=device_client_table, back_populates="Clients"
    )

    def __init__(self, name):
        self.Name = name
        self.ClientID = ""

    def json(self):
        return {
            "client_id": self.ClientID,
            "name": self.Name,
            "devices": [device.json() for device in self.Devices.all()],
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(client_id=id).first()
