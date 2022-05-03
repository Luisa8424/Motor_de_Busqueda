class Grupo:
    CodGrupo:str
    NomGrupo:str
    Programa:Programa

    def __init__(self,Estudiante,Programa):
        self.Estudiante = Estudiante
        self.Programa = Programa

        