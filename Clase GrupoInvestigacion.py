from datetime import date
from sqlite3 import Date


class GrupoInvestigacion:
    NombreGrupo: str
    FechaGrupoInvestigacion: date
    Docente: Docente ()
    
    def BuscarGrupoInvestigacion(self,nombreGrupo:str, fechaGrupoinvestigacion: date, docente: Docente ):
         """Mostrar """
       return nombreGrupo:str, fechaGrupoInvestigacion: date, docente: Docente
   
   
     
   f = open("usuarios.txt", "w")
   f.write(nombreGrupo:str, fechaGrupoinvestigacion: date, docente: Docente)
   64
   f.close()
   f=open("usuarios.txt", "a")
   f.write("agregar nombreGrupo, fechaGrupoInvestigacion, docente")
   52
   f.close()
   f = open('usuarios.txt', 'r')
   lines = f.readlines()
   
   for i in range(len(lines)):
       lines[i] = lines[i].replace('\n', '')
       lista_nombreGrupo_fechaGrupoinvestigacion_docente_ = []
   for i in lines:
       lista_nombreGrupo_fechaGrupoinvestigacion_docente.append(i.split(" "))
       nombres = []
   for i in lista_nombreGrupo_fechaGrupoinvestigacion_docente:
       nombres.append(i[0])
       nombres.sort()
       print(nombres)
       f.close()
       
   