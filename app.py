from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)
CORS(app)

# Servir o index.html
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

# Servir arquivos estáticos (CSS, JS)
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('frontend', path)

if __name__ == '__main__':
    from models import User, Product
    db.create_all()
    app.run(debug=True)
