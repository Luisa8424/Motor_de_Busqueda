from datetime import date


class Formacion:
    CodFormacion: str
    TipoFormacion: str
    NombreFormacion: str
    
        
    
    def __init__(self, Docente):
        self.Docente = Docente()
        
    def BuscarFormacion(self,codFormacion:str, tipoFormacion: str, nombreFormacion: str ):
         """Mostrar """
       return codFormacion:str, tipoFormacion: str, nombreFormacion: str
   
    def DefinirFormacion(self):
         """Mostrar """
       return DefinirFormacion
     
   f = open("usuarios.txt", "w")
   f.write(codFormacion:str, tipoFormacion: str, nombreFormacion: str)
   56
   f.close()
   f=open("usuarios.txt", "a")
   f.write("agregar codFormacion, tipoFormacion, nombreFormacion")
   52
   f.close()
   f = open('usuarios.txt', 'r')
   lines = f.readlines()
   
   for i in range(len(lines)):
       lines[i] = lines[i].replace('\n', '')
       lista_codFormacion_tipoFormacion_nombreFormacion = []
   for i in lines:
       lista_codFormacion_tipoFormacion_nombreFormacion.append(i.split(" "))
       formacion = []
   for i in lista_nombreGrupo_fechaGrupoinvestigacion_docente:
       formacion.append(i[0])
       formacion.sort()
       print(formacion)
       f.close()
       
       
