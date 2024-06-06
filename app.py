from flask import Flask
from flask_cors import CORS
from model import db
from router import api


app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(api)
db.init_app(app)
CORS(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
