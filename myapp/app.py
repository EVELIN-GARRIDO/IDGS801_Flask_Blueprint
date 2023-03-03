from flask import Flask, jsonify, render_template
from flask import request
from flask import redirect
from flask import url_for
from Alumnos.routes import alumnos
from Directivos.routes import dir
from Maestros.routes import maestros

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET','POST'])
def home():
    return jsonify({'Datos': 'Hola'})

app.register_blueprint(alumnos)
app.register_blueprint(dir)
app.register_blueprint(maestros)

if __name__ == '__main__':
    app.run()