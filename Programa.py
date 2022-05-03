class Programa :
    IdPrograma:str
    NomPrograma:str
    Certifacion:Certifacion
    
    def _int_(self, Facultad, Asignatura, Estudiante):
        self.Facultad=Facultad
        self.Asignatura=Asignatura
        self.Estudiante=Estudiante

    def BuscarPrograma(self):
        print("Definir Programa.")
Programa.BuscarPrograma()

Archivo_Programa=open("Texto_Programa.txt", "w")
Archivo_Programa.write("Motor de Búsqueda")
Archivo_Programa.write("Construimos este archivo\n")
Archivo_Programa.write("Para que nos arroje datos\n")
Archivo_Programa.write("Sobre los programas académicos de la Universidad\n")
Archivo_Programa.close()


    