class ExperienciaInvestigacion:
    AnosInvestigacion: int 
    CantidadPublicaciones: int
    TipoPublicacion: str
    Docente: Docente ()
    
def BuscarExperienciaInvestigacion(self,anosInvestigacion:int, cantidadPublicaciones: int, tipoPublicacion: str, docente: Docente):
         """Mostrar """
         return anosInvestigacion: int, cantidadPublicaciones: int, tipoPublicacion: str, docente: Docente
   
def ActualizarExperienciaInvestigacion(self, cantidaPublicaciones: int, tipoPublicion: str):
         """Mostrar """
         return cantidaPublicaciones: int, tipoPublicion: str
     
f = open("usuarios.txt", "w")
f.write(anosInvestigacion:int, cantidadPublicaciones: int, tipoPublicacion: str, docente: Docente)
87
f.close()
f=open("usuarios.txt", "a")
f.write("agregar anosInvestigacion, cantidadPublicaciones, tipoPublicaion, docente")
52
f.close()
f = open('usuarios.txt', 'r')
lines = f.readlines()
   
for i in range(len(lines)):
       lines[i] = lines[i].replace('\n', '')
       lista_anosPublicacion_cantidadPublicaiones_tipoPublicacion_docente = []
for i in lines:
       lista_anosPublicacion_cantidadPublicaiones_tipoPublicacion_docente.append(i.split(" "))
       publicaciones = []
for i in anosPublicacion_cantidadPublicaiones_tipoPublicacion_docente:
       publicaciones.append(i[0])
       publicaciones.sort()
       print(publicaciones)
       f.close()
       
       
