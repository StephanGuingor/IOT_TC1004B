import db
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

load_dotenv()

if __name__ == "__main__":
    db.init_db(app)
    app.run(port=5000, debug=True)
