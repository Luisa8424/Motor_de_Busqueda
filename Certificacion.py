from datetime import date


class Certificacion:
    FechaCertificacion:date
    Pares:str

    def BuscarCertificacion(self):
        print("Certificacion.")

Certificacion.BuscarCertificacion()
