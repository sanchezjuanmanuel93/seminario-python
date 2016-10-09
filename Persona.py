class Persona(object):

    def __init__(self, dni, nombre, apellido, edad, sexo, peso, altura):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = dni

    def esMayorEdad(self):
        return self.edad >= 18

    def printData(self):
        print(("Nombre: " + str(self.nombre)))


    def toJSON(self):
        return {
                'nombre': self.nombre,
                'apellido': self.apellido,
                'edad': self.edad,
                'sexo': self.sexo,
                'peso': self.peso,
                'altura': self.altura,
                'dni': self.dni
            }











