from decimal import Decimal
from core.domain.value_objects.temperature import Temperature
from core.domain.value_objects.temperature_scala import TemperatureScala
from core.ports.temperature_control_port import TemperatureControlPort
from core.ports.thermostat_repository import ThermostatRepository


class ThermostatController:
    temperature_control_port: TemperatureControlPort
    thermostat_repository: ThermostatRepository

    def __init__(
        self,
        temperature_control_port: TemperatureControlPort,
        thermostat_repository: ThermostatRepository,
    ) -> None:
        self.temperature_control_port = temperature_control_port
        self.thermostat_repository = thermostat_repository

    def update_temperature_of_thermostat_id(
        self,
        thermostat_id: str,
        temperature: float,
    ):
        thermostat = self.thermostat_repository.get_by_id(id=thermostat_id)

        if thermostat is None:
            raise Exception(f'Thermostat with id: "{thermostat_id}" not found!')

        self.temperature_control_port.set_temperature(
            thermostat=thermostat,
            temperature=Temperature(
                value=Decimal(f"{temperature}"), scala=TemperatureScala.CELSIUS
            ),
        )
