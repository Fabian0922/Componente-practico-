from abc import abstractmethod
from domain.base_record import RegistroClinico

class TratamientoMedico(RegistroClinico):
    """Clase abstracta para tipos de atención médica."""
    def __init__(self, descripcion, honorarios_base):
        super().__init__()
        self.descripcion = descripcion
        self.honorarios_base = honorarios_base

    @abstractmethod
    def tasar_servicio(self, **opciones):
        """Cálculo polimórfico de costos médicos."""
        pass

    @abstractmethod
    def validar_protocolo(self, **datos):
        """Validación de seguridad para el procedimiento."""
        pass