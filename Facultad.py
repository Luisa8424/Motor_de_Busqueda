class Facultdad:
    IdFacultad:str
    NombreFacultad:str
    Programa:Programa
    Departamento:Departamento
    Decano:Decano

    def BuscarFacultad(self):
        print("Definir Facultad.")
Facultdad.BuscarFacultad()

Archivo_Facultad=open("Texto_Facultad.txt", "w")
Archivo_Facultad.write("Motor de Búsqueda")
Archivo_Facultad.write("Construimos este archivo\n")
Archivo_Facultad.write("Para que nos arroje datos\n")
Archivo_Facultad.write("Sobre las facultades de la Universidad\n")
Archivo_Facultad.close()