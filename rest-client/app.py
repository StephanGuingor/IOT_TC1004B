from flask_sqlalchemy import SQLAlchemy

import db
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api

from resources.client import Client, ClientList
from resources.device import Device, DeviceList
from resources.data_record import DataRecord, DataRecordList

load_dotenv()

app = Flask(__name__)

db.init_db(app)

from models.device_ownership import device_client_table
from models.device import DeviceModel
from models.client import ClientModel
from models.data_record import DataRecordModel


db.db.create_all()

api = Api(app)


# ENDPOINTS
api.add_resource(Client, "/client/<string:client_id>")
api.add_resource(ClientList, "/clients")
api.add_resource(Device, "/device/<string:model>")
api.add_resource(DeviceList, "/devices")
api.add_resource(DataRecord, "/data-record/<string:record_id>")
api.add_resource(DataRecordList, "/data-records")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
