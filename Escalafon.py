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

Archivo_3=open("Texto Escalafon", "w")
Archivo_3.write("MOTOR DE BUSQUEDA")
Archivo_3.write("Por medio de este texto \n")
Archivo_3.write("almacenaremos todos los datos \n")
Archivo_3.write("que sean consultados para \n")
Archivo_3.write("la clase escalafon.")
Archivo_3.close()