from PersonaDatos import PersonaDatos
import json
from flask import jsonify
#from Persona import Persona

a = PersonaDatos()
#p = a.get(37448343)
#dni      | nombre      | apellido | edad | sexo | peso | altura
#persona = Persona(37448344, "JuanCHO23", "Sanchez", 23, 'M', 68.3, 1.72)

#if a.update(persona):
    #print("Se actualizo bien la persona '%s'" % persona.nombre)
#else:
    #print("Error al actualizose la persona")

personas = a.getAll()
results = [persona.toJSON() for persona in personas ]

# str = jsonify(persona)
print(results)
# for p in personas:
    # print(p.nombre)
