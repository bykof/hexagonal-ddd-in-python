from abc import ABC, abstractmethod

from core.domain.entities.thermostat import Thermostat
from core.domain.value_objects.temperature import Temperature


class TemperatureControlPort(ABC):
    @abstractmethod
    def set_temperature(self, thermostat: Thermostat, temperature: Temperature):
        pass
