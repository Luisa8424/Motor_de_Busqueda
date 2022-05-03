class Programa :
    IdPrograma:str
    NomPrograma:str
    Certifacion:Certifacion
    
    def _int_(self, Facultad, Asignatura, Estudiante):
        self.Facultad=Facultad
        self.Asignatura=Asignatura
        self.Estudiante=Estudiante

    