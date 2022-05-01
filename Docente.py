class Docente(Usuario):
    Programa:Programa
    ExperienciaProfesional:ExperienciaProfesional
    Experienciainvestigacion:Experienciainvestigacion
    ExperienciaDocente:ExperienciaDocente
    Apoyo:Apoyo
    LaborExtracurricular:LaborExtracurricular
    Formacion:Formacion
    Escalafon:Escalafon
    
    def __init__(self,Programa,Asignatura):
        self.Programa = Programa
        self.Asignatura = Asignatura
