from PersonaDatos import PersonaDatos
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
for p in personas:
    print(p.nombre)
