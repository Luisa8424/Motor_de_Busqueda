from datetime import date
from sqlite3 import Date


class LaborExtracurricular:
    LugarDesempeno: str
    Cargo: str
    FechaLabor: date
    Docente: Docente ()
    
    def BuscarLaborExtracurricular(self,lugarDesempeno:str, cargo: str, fechaLabor: str, docente: Docente ):
         """Mostrar """
       return LugarDesempeno:str, cargo: str, fechaLabor: str, docente: Docente
   
   f = open("usuarios.txt", "w")
       f.write(lugarDesempeno:str, cargo: str, fechaLabor: str, docente: Docente)
       63
       f.close()
       f=open("usuarios.txt", "a")
       f.write("agregar lugarDesempeno, cargo, fechaLabor, docente")
       47
       f.close()
       f = open('usuarios.txt', 'r')
       
       lines = f.readlines()
       
       
       for i in range(len(lines)):
           lines[i] = lines[i].replace('\n', '')
           
           lista_lugarDesempeno_cargo_fechaLabor_docente = []
           for i in lines:
               lista_lugarDesempeno_cargo_fechaLabor_docente.append(i.split(" "))
               nombres = []
               for i in lista_lugarDesempeno_cargo_fechaLabor_docente:
                   nombres.append(i[0])
                   nombres.sort()
                   print(nombres)
                   f.close()
       