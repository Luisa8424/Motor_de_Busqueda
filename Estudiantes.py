class Estudiantes:
    CodEstudiante:str
    Programa:Programa
    Asignatura:Asignatura
    
    def __init__(self,Asignatura):
        self.Asignatura=Asignatura

    def BuscarEstudiante(self):
        print("BuscarEstudiante. ")

Estudiantes.BuscarEstudiante()