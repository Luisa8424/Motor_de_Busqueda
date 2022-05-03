class Usuario:
    Id:str
    Nombre:str
    TipoContratacion:str
    MaximoNivelFormacion:str
    HorasDedicacion:str
    Cargo:str
    
    def __init__(self,Departamento):
        self.Departamento = Departamento()