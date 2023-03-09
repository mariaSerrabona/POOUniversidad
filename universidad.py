

class Miembro():
    def __init__(self, nombre, edad, dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni


class Profesor(Miembro):
    def __init__(self, nombre, edad, dni, num_registro, asiganturas):
        Miembro.__init__(self, nombre, edad, dni)
        self.num_registro=num_registro
        self.asiganturas=asiganturas

    def añade_docencia(self, docencia):
        self.asignaturas=[]
        self.asignaturas.append(docencia)



class Alumno(Miembro):
    def __init__(self, nombre, edad, dni, num_estudiante, asignaruras):
        Miembro.__init__(self, nombre, edad, dni)
        self.num_estudiante=num_estudiante
        self.asignaruras=asignaruras
