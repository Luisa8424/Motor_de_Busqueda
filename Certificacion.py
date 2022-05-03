from datetime import date


class Certificacion:
    FechaCertificacion:date
    Pares:str
    Programa:Programa

    def BuscarCertificacion(self):
        print("Certificacion.")

Certificacion.BuscarCertificacion()
