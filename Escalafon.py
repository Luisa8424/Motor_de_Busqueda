class Escalafon:
    CodEscalafon:str
    TipoEscalafon:str

    def __init__(self,Docente):
        self.Docente = Docente
        
    def BuscarEscalafon(self):
        print("BuscarEscalafon. ")

    def DefinirEscalafon(self):
        print("SeDefinio. ")

Escalafon.BuscarEscalafon()
Escalafon.DefinirEscalafon()