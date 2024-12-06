import typing
from core.domain.entities.thermostat import Thermostat
from core.ports.thermostat_repository import ThermostatRepository


class LocalThermostatRepository(ThermostatRepository):
    thermostats: typing.List[Thermostat]

    def __init__(self) -> None:
        super().__init__()
        self.thermostats = []

    def add(self, thermostats: typing.List[Thermostat]):
        self.thermostats += thermostats

    def get_by_id(self, id: str) -> Thermostat | None:
        for thermostat in self.thermostats:
            if thermostat.id == id:
                return thermostat
        return None

    def get_all(self) -> typing.List[Thermostat]:
        return self.thermostats.copy()
