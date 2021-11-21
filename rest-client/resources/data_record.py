from flask_restful import Resource, reqparse
from sqlalchemy.exc import SQLAlchemyError
from models.data_record import DataRecordModel

ERR_NOT_FOUND = ({"message": "Element not found"}, 404)


parser = reqparse.RequestParser()
parser.add_argument(
    "humidity",
    type=int,
    required=False,
)

parser.add_argument(
    "gas_concentration",
    type=int,
    required=True,
    help="gas_concentration is required.",
)

parser.add_argument(
    "temperature",
    type=int,
    required=False,
)

parser.add_argument(
    "client_id",
    type=str,
    required=True,
    help="Every data record should be linked to a client.",
)

parser.add_argument(
    "model",
    type=str,
    required=True,
    help="Every data record should be linked to a model.",
)


class DataRecord(Resource):
    @staticmethod
    def get(record_id):
        record = DataRecordModel.find_by_id(record_id)
        if record:
            return record.json()
        return ERR_NOT_FOUND


class DataRecordList(Resource):
    @staticmethod
    def get():
        return {
            "data_records": list(map(lambda x: x.json(), DataRecordModel.query.all()))
        }, 200

    @staticmethod
    def post():
        data = parser.parse_args()

        record = DataRecordModel(**data)

        try:
            record.save_to_db()
        except Exception as e:
            return {f"An error ocurred: {e}"}, 500

        return record.json(), 201
