class VitalisHubError(Exception):
    """Error base del sistema Vitalis."""
    def __init__(self, detail, source_error=None):
        super().__init__(detail)
        self.source_error = source_error

class InvalidPatientData(VitalisHubError):
    """Lanzada cuando los datos del paciente son inconsistentes."""
    pass

class MedicalConflictError(VitalisHubError):
    """Lanzada ante errores de lógica clínica o financiera."""
    pass

class AgendaCapacityExceeded(VitalisHubError):
    """Lanzada cuando no hay cupo para un tratamiento."""
    pass