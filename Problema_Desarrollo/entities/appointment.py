from core_exceptions.medical_errors import MedicalConflictError

class CitaMedica:
    def __init__(self, paciente, tratamiento, specs):
        self.paciente = paciente
        self.tratamiento = tratamiento
        self.specs = specs
        self.confirmada = False

    def autorizar_cita(self):
        try:
            self.tratamiento.validar_protocolo(**self.specs)
            self.costo_final = self.tratamiento.tasar_servicio(**self.specs)
            self.confirmada = True
            print(f"Cita Autorizada Folio: {self.tratamiento.folio}")
        except Exception as e:
            raise MedicalConflictError(f"Denegación de Cita: {str(e)}") from e