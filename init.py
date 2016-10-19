from flask import Flask, redirect
from flask import render_template
from flask import jsonify
import json
from flask import request
from PersonaDatos import PersonaDatos
from wtforms import Form, StringField, IntegerField, validators, RadioField, FloatField
from Persona import Persona

app = Flask(__name__)

personaDatos = PersonaDatos()


class RegistraPersonaForm(Form):
    nombre = StringField('Nombre', [validators.Length(min=4, max=30, message="El NOMBRE debe contener por lo menos 4 caracteres y como maximo 30")])
    apellido = StringField('Apellido', [validators.Length(min=4, max=30, message="El APELLIDO debe contener por lo menos 4 caracteres y como maximo 30")])
    edad = IntegerField('edad', [validators.NumberRange(min=1, max=100,message="Ingrese una edad correcta")])
    sexo = RadioField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')])
    peso = FloatField('Peso')
    altura = FloatField('Altura')
    dni = IntegerField('Dni', [validators.NumberRange(min=1000000, max=100000000,message="Ingrese un DNI correcto")])


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/personas/')
def personasAll():
    personas = personaDatos.getAll()
    return render_template('persona/personas.html', personas=personas)


@app.route('/personas/agregar', methods=['GET', 'POST'])
def personasAgregar():
    form = RegistraPersonaForm(request.form)
    if request.method == 'POST' and form.validate():
        persona = Persona(form.dni.data, form.nombre.data, form.apellido.data, form.edad.data, form.sexo.data,
                          form.peso.data, form.altura.data)
        if personaDatos.insert(persona):
            return redirect("/personas/")
        else:
            return redirect("/personas/agregar")
    return render_template('persona/agregarPersona.html', form=form)


@app.route('/api/personas/')
def personasAllAPI():
    personas = personaDatos.getAll()
    jsonStr = json.dumps([e.toJSON() for e in personas])
    return jsonStr


@app.route('/api/personas/<int:dni>')
def personasGetAPI(dni):
    return jsonify(personaDatos.get(dni).toJSON())


@app.route('/personas/jquery')
def jsonStatic():
    return render_template('persona/jquery.html')


if __name__ == "__main__":
    app.run(debug=True)
