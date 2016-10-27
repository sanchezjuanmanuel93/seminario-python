# Librerias basicas para montar el servidor y renderizar las vistar
from flask import Flask, redirect,request,render_template

# Importamos las librerias para devolver un objeto JSON
from flask import jsonify
import json

# Entidad Persona
from Persona import Persona

# Acceso a datos
from PersonaDatos import PersonaDatos

# Liberia para renderizar el formulario con la validaciones especificadas
from wtforms import Form, StringField, IntegerField, validators, RadioField, FloatField


app = Flask(__name__)

# Instacia para acceder a los datos
personaDatos = PersonaDatos()

# Se crea la clase que luego se renderiza como un formulario con los campos y validaciones especificadas
class RegistraPersonaForm(Form):
    nombre = StringField('Nombre', [validators.Length(min=4, max=30, message="El NOMBRE debe contener por lo menos 4 caracteres y como maximo 30")])
    apellido = StringField('Apellido', [validators.Length(min=4, max=30, message="El APELLIDO debe contener por lo menos 4 caracteres y como maximo 30")])
    edad = IntegerField('edad', [validators.NumberRange(min=1, max=100,message="Ingrese una edad correcta")])
    sexo = RadioField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')])
    peso = FloatField('Peso')
    altura = FloatField('Altura')
    dni = IntegerField('Dni', [validators.NumberRange(min=1000000, max=100000000,message="Ingrese un DNI correcto")])

# Pagina principal
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Muestra listado de personas mediante JINJA2(VER personas.html)
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

# EJEMPLO API REST

# Devuelve un arreglo JSON con el contenido de todas las personas
@app.route('/api/personas/')
def personasAllAPI():
    personas = personaDatos.getAll()
    jsonStr = json.dumps([e.toJSON() for e in personas])
    return jsonStr

# Devuelve un objecto JSON con el contenido de la persona con dni especificado por parametro
@app.route('/api/personas/<int:dni>')
def personasGetAPI(dni):
    return jsonify(personaDatos.get(dni).toJSON())

# Muestra listado de personas mediante jQuery(VER jquery.html)
@app.route('/personas/jquery')
def jsonStatic():
    return render_template('persona/jquery.html')



if __name__ == "__main__":
    app.run(debug=True)
