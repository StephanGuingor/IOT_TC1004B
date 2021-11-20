from DB import *
from Models import *

app = Flask(__name__)

if __name__ == "__main__":
    innit_app(app)
    app.run(port=5000, debug=True)



