from abc import ABC
from datetime import datetime
import secrets

class RegistroClinico(ABC):
    """Abstracción para cualquier registro dentro del Hub."""
    def __init__(self):
        self._folio_interno = secrets.token_hex(4).upper()
        self._timestamp = datetime.now()

    @property
    def folio(self): return self._folio_interno