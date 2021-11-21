from flask_sqlalchemy import SQLAlchemy
from os import environ

db = SQLAlchemy()

SQL_USER = "SQL_USER"
SQL_PASSWORD = "SQL_PASSWORD"
SQL_PORT = "SQL_PORT"
SQL_DB = "SQL_DB"


def init_db(app):
    user = environ.get(SQL_USER, "")
    password = environ.get(SQL_PASSWORD, "")
    port = environ.get(SQL_PORT, "")
    database = environ.get(SQL_DB, "")

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mariadb+mariadbconnector://test:test@mariadb:3306/test"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    global db
    db = SQLAlchemy(app)
