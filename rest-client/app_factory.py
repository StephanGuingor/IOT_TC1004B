from flask import Flask
from flask_restful import Api

from resources.client import Client, ClientList
from resources.device import Device, DeviceList
from resources.data_record import DataRecord, DataRecordList
from resources.owner import Owner

from db import db


def create_app():

    app = Flask(__name__)
    api = Api(app)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mariadb+mariadbconnector://test:test@mariadb:3306/test"  # should secure!
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ENDPOINTS
    api.add_resource(Client, "/client/<string:client_id>")
    api.add_resource(ClientList, "/clients")
    api.add_resource(Device, "/device/<string:model>")
    api.add_resource(DeviceList, "/devices")
    api.add_resource(DataRecord, "/data-record/<string:record_id>")
    api.add_resource(DataRecordList, "/data-records")
    api.add_resource(Owner, "/ownership")

    db.init_app(app)

    @app.shell_context_processor
    def shell_context():
        return {"db": db}

    @app.before_first_request
    def create_handle():
        db.create_all()

    return app
