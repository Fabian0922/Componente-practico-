import re
from core_exceptions.medical_errors import InvalidPatientData

class Paciente:
    def __init__(self, id_medico, nombre_completo, contacto_email):
        self.__id_medico = self.__sanitizar_id(id_medico)
        self.nombre_completo = nombre_completo
        self.__contacto_email = self.__validar_correo(contacto_email)

    def __sanitizar_id(self, valor):
        if not str(valor).isalnum():
            raise InvalidPatientData(f"ID Médico '{valor}' debe ser alfanumérico.")
        return valor

    def __validar_correo(self, correo):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            raise InvalidPatientData(f"Correo electrónico inválido: {correo}")
        return correo

    @property
    def identificacion(self): return self.__id_medico