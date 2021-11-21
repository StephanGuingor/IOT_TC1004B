from flask_restful import Resource, reqparse
from models.client import ClientModel

ERR_NOT_FOUND = ({"message": "Element not found"}, 404)

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="name is required")


class Client(Resource):
    @staticmethod
    def get(client_id):
        client = ClientModel.find_by_id(client_id)
        if client:
            return client.json()
        return ERR_NOT_FOUND


class ClientList(Resource):
    @staticmethod
    def get():
        return {"clients": list(map(lambda x: x.json(), ClientModel.query.all()))}, 200

    @staticmethod
    def post():
        data = parser.parse_args()

        client = ClientModel(**data)

        try:
            client.save_to_db()
        except Exception as e:
            return {"message": f"An error ocurred: {e}"}, 500

        return client.json(), 201
