from domain.medical_service import TratamientoMedico
from core_exceptions.medical_errors import MedicalConflictError

class Telemedicina(TratamientoMedico):
    def tasar_servicio(self, minutos=20, nocturno=False):
        # Sobrecarga: Recargo por horario nocturno
        factor = 1.5 if nocturno else 1.0
        return self.honorarios_base * factor * (minutos / 20)

    def validar_protocolo(self, **datos):
        if not datos.get('conexion_estable', False):
            raise MedicalConflictError("Fallo de protocolo: Requiere conexión estable.")

class ProcedimientoQuirurgico(TratamientoMedico):
    def tasar_servicio(self, complejidad=1, insumos=0):
        # Sobrecarga: Basado en nivel de riesgo e insumos
        return (self.honorarios_base * complejidad) + insumos

    def validar_protocolo(self, **datos):
        if not datos.get('ayuno_completo', False):
            raise MedicalConflictError("Riesgo Clínico: Paciente no cumple ayuno.")

class ExamenLaboratorio(TratamientoMedico):
    def tasar_servicio(self, cobertura_seguro=0.20):
        return self.honorarios_base * (1 - cobertura_seguro)

    def validar_protocolo(self, **datos):
        pass