from flask import Flask
from flask import render_template
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

if __name__ == "__main__":
    app.run(debug=True)