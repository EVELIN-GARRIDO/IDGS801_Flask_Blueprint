from flask import Blueprint

maestros = Blueprint('maestros', __name__)

@maestros.route('/getmaes', methods = ['GET'])
def getmaes():
    return {'key': 'Maestros'}