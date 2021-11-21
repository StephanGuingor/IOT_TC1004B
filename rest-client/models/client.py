from db import db
from models.base_model import BaseModel

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
        "DeviceModel", secondary="device_client_table", back_populates="Clients"
    )

    def __init__(self, name):
        self.Name = name

    def json(self, local=True):
        m = {"client_id": self.ClientID, "name": self.Name}

        if local:
            m["devices"] = [device.json(False) for device in self.Devices]

        return m

    @classmethod
    def find_by_id(cls, id) -> "ClientModel":
        return cls.query.filter_by(ClientID=id).first()
