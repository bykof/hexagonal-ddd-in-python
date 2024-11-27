from abc import ABC, abstractmethod

from core.domain.entities.thermostat import Thermostat
from core.domain.value_objects.temperature import Temperature
from core.domain.value_objects.thermostat_port_type import ThermostatPortType


class ThermostatPort(ABC):
    @abstractmethod
    def update_temperature(self, thermostat: Thermostat, temperature: Temperature):
        pass

    @abstractmethod
    def port_type(self) -> ThermostatPortType:
        pass
