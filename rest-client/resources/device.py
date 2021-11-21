from flask_restful import Resource, reqparse
from models.device import DeviceModel

ERR_NOT_FOUND = ({"message": "Element not found"}, 404)

parser = reqparse.RequestParser()
parser.add_argument(
    "model",
    type=int,
    required=False,
)

parser.add_argument(
    "pre_heat_time", type=int, required=True, help="gas_concentration is required."
)

parser.add_argument(
    "ideal_humidity",
    type=int,
    required=False,
)

parser.add_argument(
    "ideal_temperature",
    type=str,
    required=True,
    help="Every data record should be linked to a client.",
)


class Device(Resource):
    def get(self, model):
        device = DeviceModel.find_by_model(model)

        if device:
            return device.json()
        return ERR_NOT_FOUND


class DeviceList(Resource):
    def get(self):
        return {
            "devices": list(map(lambda x: x.json(), DeviceModel.query.all()))
        }, 200  # filter by client ?

    def post(self):
        data = Device.parser.parse_args()

        device = DeviceModel(**data)

        try:
            device.save_to_db()
        except Exception as e:
            return {f"An error ocurred: {e}"}, 500

        return device.json(), 201
