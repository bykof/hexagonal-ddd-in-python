from core.domain.entities.thermostat import Thermostat
from core.domain.value_objects.temperature import Temperature
from core.domain.value_objects.thermostat_port_type import ThermostatPortType
from core.ports.thermostat_port import ThermostatPort


class UartThermostatAdapter(ThermostatPort):
    def update_temperature(self, thermostat: Thermostat, temperature: Temperature):
        print(f"Updating temperature of {thermostat.id} to {temperature} via UART")

    def port_type(self) -> ThermostatPortType:
        return ThermostatPortType.UART
