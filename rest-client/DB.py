from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_expects_json import expects_json

db=SQLAlchemy()

def innit_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reto.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    global db
    db=SQLAlchemy(app)
    db.create_all()
    