class Docente(Usuario):
    ExperienciaProfesional:ExperienciaProfesional
    ExperienciaInvestigacion:ExperienciaInvestigacion
    ExperienciaDocente:ExperienciaDocente
    Apoyo:Apoyo
    GrupoInvestigacion:GrupoInvestigacion
    LaborExtracurricular:LaborExtracurricular
    Formacion:Formacion
    Escalafon:Escalafon

    def __init__(self,ExperienciaProfesional, ExperienciaDocente, Escalafon, Formacion):
        self.ExperienciaProfesional = ExperienciaProfesional
        self.ExperienciaDocente = ExperienciaDocente
        self.Escalafon = Escalafon
        self.Formacion = Formacion

    def BuscarDocente(self):
        print("BuscarDocente.")

    def InactivarDocente(self):
        print("Desactivado")

    def ActualizarDocente(self):
        print("Actualizado")
    
Docente.BuscarDocente()
Docente.InactivarDocente()
Docente.ActualizarDocente()
    

