class Grupo:
    CodGrupo:str
    NomGrupo:str
    Asignatura:Asignatura

    def __init__(self,Asignatura):
        self.Asignatura = Asignatura
        
    def CrearGrupo(self):
        print("CrearGrupo. ")

    def DefinirGrupo(self):
        print("DefinirGrupo. ")

    def ModificarGrupo(self):
        print("Modificado. ")

Grupo.CrearGrupo()
Grupo.DefinirGrupo()
Grupo.ModificarGrupo()

        