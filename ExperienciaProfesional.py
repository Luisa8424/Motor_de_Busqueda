class ExperienciaProfesional:
    AnosProfesiona:int

    def __init__(self,Docente):
        self.Docente = Docente

    def BuscarExperienciaProfesiona(self):
        print("BuscarExperienciaProfesiona. ")

    def ActualizarExperienciaProfesional(self):
        print("Actualizado. ")

ExperienciaProfesional.BuscarExperienciaProfesiona()
ExperienciaProfesional.ActualizarExperienciaProfesional()

Archivo_2=open("Texto_Experiencia", "w")
Archivo_2.write("MOTOR DE BUSQUEDA")
Archivo_2.write("aqui quedaran almacenadas \n")
Archivo_2.write("todas las consultas que se realicen \n")
Archivo_2.write("para la clase Experiencia Profesional \n")
Archivo_2.close()