from Conexion import Conexion
from Persona import Persona

class PersonaDatos(Conexion):

    def __init__(self):
        super(PersonaDatos, self).__init__()

    def get(self, dni):

        sql = "SELECT * FROM persona WHERE dni = %d" %dni
        p = super(PersonaDatos, self).executeOneQuery(sql)
        if p:
            return Persona(p[0],p[1],p[2],p[3],p[4],p[5],p[6])

    def insert(self, persona):
        sql = """INSERT INTO persona(dni,nombre,apellido,edad,sexo,peso,altura) VALUES(%d, '%s', '%s', %d, '%c', %f, %f)""" % (persona.dni, persona.nombre, persona.apellido, persona.edad, persona.sexo, persona.peso, persona.altura)
        return super(PersonaDatos, self).executeNonQuery(sql)

    def update(self, persona):
        sql = """UPDATE persona SET nombre = '%s', apellido = '%s', edad = %d, sexo = '%c', peso = %f, altura = %f WHERE dni = %d""" % (persona.nombre, persona.apellido, persona.edad, persona.sexo, persona.peso, persona.altura, persona.dni)
        return super(PersonaDatos, self).executeNonQuery(sql)

    def getAll(self):
        personas = []
        sql = "SELECT * FROM persona"
        ps = super(PersonaDatos, self).executeQuery(sql)
        #print((len(ps)))
        for p in ps:
            per = Persona(p[0], p[1], p[2], p[3], p[4], p[5], p[6])
            personas.append(per)
        return personas

