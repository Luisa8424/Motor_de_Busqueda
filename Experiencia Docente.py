class ExperienciaDocente:
    LugarTrabajo:str
    FechaExperienciaDocente:Date
    AnosDocente:int
    def _int_(self, Docente):
        self.Docente=Docente

    def ExperienciaDocente(self):
        print("Actualizar Docente Tipo Experiencia.")
ExperienciaDocente.ExperienciaDocente()