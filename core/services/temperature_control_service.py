import typing
from core.domain.entities.thermostat import Thermostat
from core.domain.value_objects.temperature import Temperature
from core.domain.value_objects.thermostat_port_type import ThermostatPortType
from core.ports.temperature_control_port import TemperatureControlPort
from core.ports.thermostat_port import ThermostatPort


class TemperatureControlService(TemperatureControlPort):
    thermostat_ports_mapping: typing.Dict[ThermostatPortType, ThermostatPort]

    def __init__(self, thermostat_ports: typing.List[ThermostatPort]) -> None:
        super().__init__()
        self.thermostat_ports_mapping = {
            thermostat_port.port_type(): thermostat_port
            for thermostat_port in thermostat_ports
        }

    def set_temperature(self, thermostat: Thermostat, temperature: Temperature):
        thermostat_port = self.thermostat_ports_mapping.get(thermostat.port_type)
        if thermostat_port is None:
            raise Exception(
                f"Thermostat: {thermostat} has no supported thermostat_port"
            )

        thermostat_port.update_temperature(
            thermostat=thermostat, temperature=temperature
        )
