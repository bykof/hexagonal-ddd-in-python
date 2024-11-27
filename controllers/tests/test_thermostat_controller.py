from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock

from controllers.thermostat_controller import ThermostatController
from core.domain.entities.thermostat import Thermostat
from core.domain.value_objects.temperature import Temperature
from core.domain.value_objects.temperature_scala import TemperatureScala
from core.domain.value_objects.thermostat_port_type import ThermostatPortType


class TestThermostatController(TestCase):
    def test_update_temperature_of_thermostat_id_sucess(self):
        temperature_control_port = MagicMock()
        thermostat_repository = MagicMock()

        thermostat = Thermostat(id="123", port_type=ThermostatPortType.API)
        thermostat_repository.get_by_id = MagicMock(return_value=thermostat)

        temperature_control_port.set_temperature = MagicMock()

        thermostat_controller = ThermostatController(
            temperature_control_port=temperature_control_port,
            thermostat_repository=thermostat_repository,
        )
        temperature = 21.5

        thermostat_controller.update_temperature_of_thermostat_id(
            thermostat_id=thermostat.id, temperature=temperature
        )
        thermostat_repository.get_by_id.assert_called_once_with(id=thermostat.id)

        temperature_control_port.set_temperature.assert_called_once_with(
            thermostat=thermostat,
            temperature=Temperature(
                value=Decimal(f"{temperature}"), scala=TemperatureScala.CELSIUS
            ),
        )
