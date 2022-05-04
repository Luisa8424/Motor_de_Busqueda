class Estudiantes:
    CodEstudiante:str
    Programa:Programa
    Asignatura:Asignatura
    
    def __init__(self,Asignatura,Programa):
        self.Asignatura=Asignatura
        self.Programa = Programa

    def BuscarEstudiante(self):
        print("BuscarEstudiante. ")

Estudiantes.BuscarEstudiante()