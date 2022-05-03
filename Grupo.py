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

archivo=open("archivo_1.txt", "w")
archivo.write("MOTOR DE BUSQUEDA")
archivo.write("Hacemos este archivo\n")
archivo.write("para almacenar datos\n")
archivo.write("con respecto a la clase grupo.\n")
archivo.close()