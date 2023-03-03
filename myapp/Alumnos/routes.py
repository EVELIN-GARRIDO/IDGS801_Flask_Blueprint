from flask import Blueprint

alumnos = Blueprint('alumnos',__name__)

@alumnos.route('/getalum', methods = ['GET'])
def getalum():
    return {'key': 'Alumnos'}

