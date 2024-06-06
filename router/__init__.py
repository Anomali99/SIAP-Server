from flask import Blueprint, jsonify
api = Blueprint('router', __name__)



def handle_options():
    response = jsonify({'message': 'OPTIONS request received'})
    response.headers['Allow'] = 'POST' 
    return response, 200

from . import asatidz
from . import santri
from . import staff