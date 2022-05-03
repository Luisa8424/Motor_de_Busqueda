from inspect import _void


class Usuario:
    Id:str
    Nombre:str
    TipoContratacion:str
    MaximoNivelFormacion:str
    HorasDedicacion:str
    Cargo:str
    
    def __init__(self,Departamento):
        self.Departamento = Departamento()
        
           
    def ActualizarUsuario(self,id:str, nombre: str, tipoContratacion: str, maximoNivelformacion:str, cargo: str ):
...         """Mostrar """
...         return id:str, nombre: str, tipoContratacion: str, maximoNivelformacion:str, cargo: str

    def CrearUsuario(self,void):
...         """Mostrar """
...         return _void
       f = open("usuarios.txt", "w")
       f.write(id:str, nombre: str, tipoContratacion: str, maximoNivelformacion:str, cargo: str)
       80
       f.close()
       f=open("usuarios.txt", "a")
       f.write("agregar usuario")
       15
       f.close()
       f = open('usuarios.txt', 'r')
       
       lines = f.readlines()
       
       
       for i in range(len(lines)):
           lines[i] = lines[i].replace('\n', '')
           
           lista_id_nombre_tipoContratacion_maximoNivelFormacion_cargo = []
           for i in lines:
               lista_id_nombre_tipoContratacion_maximoNivelFormacion_cargo.append(i.split(" "))
               nombres = []
               for i in lista_id_nombre_tipoContratacion_maximoNivelFormacion_cargo:
                   nombres.append(i[0])
                   nombres.sort()
                   print(nombres)
                   f.close()
       