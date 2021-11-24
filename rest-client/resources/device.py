from flask_restful import Resource, reqparse
from models.device import DeviceModel

ERR_NOT_FOUND = ({"message": "Element not found"}, 404)

parser = reqparse.RequestParser()
parser.add_argument("model", type=str, required=True, help="model is required")

parser.add_argument(
    "pre_heat_time", type=int, required=True, help="pre_heat_time is required."
)

parser.add_argument(
    "ideal_humidity",
    type=float,
    required=False,
)

parser.add_argument("ideal_temperature", type=float, required=False)


class Device(Resource):
    @staticmethod
    def get(model):
        device = DeviceModel.find_by_model(model)

        if device:
            return device.json()
        return ERR_NOT_FOUND


class DeviceList(Resource):
    @staticmethod
    def get():
        return {
            "devices": list(map(lambda x: x.json(), DeviceModel.query.all()))
        }, 200  # filter by client ?

    @staticmethod
    def post():
        data = parser.parse_args()

        device = DeviceModel(**data)

        try:
            device.save_to_db()
        except Exception as e:
            return {"message": f"An error ocurred: {e}"}, 500

        return device.json(), 201
