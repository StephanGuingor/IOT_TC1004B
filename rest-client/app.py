from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_expects_json import expects_json
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reto.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
db.create_all()

schema = {
    'type': 'object',
    'properties': {
        'valor': {'type': 'number'},
    },
    'required': ['valor']
}

class Mediciones(db.Model):
    idMedicion= db.Column('idMedicion', db.Integer,primary_key=True)
    valor = db.Column('valor', db.Float, nullable=False)
    tsMedicion = db.Column('tsMedicion', db.DateTime(timezone=True), default=datetime.utcnow)


    def __init__(self, valor):
        self.valor=valor

db.create_all()

@app.route("/agregar", methods=["POST"])
@expects_json(schema)
def push_data():
    content= request.json

    # Agregar data a DB
    db.session.add(Mediciones(valor = content["valor"]))
    db.session.commit()

    #Respuesta
    response= jsonify({"message":"Success"})
    response.status_code=201
    return response

@app.route("/imprimir", methods=["GET"])
def get_data():
    meds=Mediciones.query.order_by(Mediciones.tsMedicion).all()
    json_meds={}
    for med in meds:
        json_meds[med.idMedicion]= ({"valor":med.valor}, {"fecha":med.tsMedicion.date()})
    response= jsonify(json_meds)
    response.status_code=200
    return response

if __name__ == "__main__":
    app.run(port=5000, debug=True)



