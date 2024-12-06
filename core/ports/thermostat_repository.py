from abc import ABC, abstractmethod
import typing

from core.domain.entities.thermostat import Thermostat


class ThermostatRepository(ABC):
    @abstractmethod
    def add(self, thermostats: typing.List[Thermostat]):
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Thermostat | None:
        pass

    @abstractmethod
    def get_all(self) -> typing.List[Thermostat]:
        pass
