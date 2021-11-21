from flask_restful import Resource, reqparse
from models.device import DeviceModel
from models.client import ClientModel


ERR_NOT_FOUND = ({"message": "Element not found"}, 404)

parser = reqparse.RequestParser()
parser.add_argument("model", type=str, required=True, help="model is required")

parser.add_argument("client_id", type=int, required=True, help="client is required.")


class Owner(Resource):
    @staticmethod
    def post():
        data = parser.parse_args()

        device = DeviceModel.find_by_model(data["model"])  # validate
        client = ClientModel.find_by_id(data["client_id"])  # validate

        if device is None or client is None:
            return ERR_NOT_FOUND

        client.Devices.append(device)
        device.Clients.append(client)

        try:
            client.save_to_db()
            device.save_to_db()

        except Exception as e:
            return {"message": f"An error ocurred: {e}"}, 500

        return {"message": "success"}, 201
