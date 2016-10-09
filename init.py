from django.http import HttpResponse
from flask import Flask
from flask import render_template
from flask import jsonify
import json
from PersonaDatos import PersonaDatos

app = Flask(__name__)

personaDatos = PersonaDatos()


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/personas/')
def personasAll():
    personas = personaDatos.getAll()
    return render_template('persona/personas.html', personas=personas)


@app.route('/api/personas/')
def personasAllAPI():
    personas = personaDatos.getAll()
    jsonStr = json.dumps([e.toJSON() for e in personas])
    return jsonStr

@app.route('/api/personas/<int:dni>')
def personasGetAPI(dni):
    return jsonify(personas = personaDatos.get(dni).toJSON())

if __name__ == "__main__":
    app.run(debug=True)
