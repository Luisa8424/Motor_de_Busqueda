class ExperienciaDocente:
    LugarTrabajo:str
    FechaExperienciaDocente:Date
    AnosDocente:int
    def _int_(self, Docente):
        self.Docente=Docente

    def ExperienciaDocente(self):
        print("Actualizar Docente Tipo Experiencia.")
ExperienciaDocente.ExperienciaDocente()

Archivo_Docente=open("Texto_Docente.txt", "w")
Archivo_Docente.write("Motor de Búsqueda")
Archivo_Docente.write("Construimos este archivo\n")
Archivo_Docente.write("Para que nos arroje datos\n")
Archivo_Docente.write("Sobre los docentes de la Universidad y validar si están certificados\n")
Archivo_Docente.close()