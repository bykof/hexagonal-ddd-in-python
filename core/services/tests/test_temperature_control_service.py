from decimal import Decimal
from unittest import TestCase
from unittest.mock import MagicMock


from core.domain.entities.thermostat import Thermostat
from core.domain.value_objects.temperature import Temperature
from core.domain.value_objects.temperature_scala import TemperatureScala
from core.domain.value_objects.thermostat_port_type import ThermostatPortType
from core.ports.thermostat_port import ThermostatPort
from core.services.temperature_control_service import TemperatureControlService


class TestTemperatureControlService(TestCase):
    def test_mapping_successful(self):
        mock_thermostat_port: MagicMock[ThermostatPort] = MagicMock(ThermostatPort)
        mock_thermostat_port.port_type = MagicMock(
            side_effect=lambda: ThermostatPortType.API
        )
        mock_thermostat_port.update_temperature = MagicMock()

        thermostat = Thermostat(id="123", port_type=ThermostatPortType.API)
        temperature = Temperature(
            value=Decimal("0"),
            scala=TemperatureScala.CELSIUS,
        )

        temperature_control_service = TemperatureControlService(
            thermostat_ports=[mock_thermostat_port]
        )
        temperature_control_service.set_temperature(
            thermostat=thermostat,
            temperature=temperature,
        )

        mock_thermostat_port.port_type.assert_called_once()
        mock_thermostat_port.update_temperature.assert_called_once_with(
            thermostat=thermostat, temperature=temperature
        )

    def test_mapping_exception(self):
        mock_thermostat_port: MagicMock[ThermostatPort] = MagicMock(ThermostatPort)
        mock_thermostat_port.port_type = MagicMock(
            side_effect=lambda: ThermostatPortType.API
        )
        mock_thermostat_port.update_temperature = MagicMock()

        thermostat = Thermostat(id="123", port_type=ThermostatPortType.UART)
        temperature = Temperature(
            value=Decimal("0"),
            scala=TemperatureScala.CELSIUS,
        )

        temperature_control_service = TemperatureControlService(
            thermostat_ports=[mock_thermostat_port]
        )

        with self.assertRaises(Exception):
            temperature_control_service.set_temperature(
                thermostat=thermostat,
                temperature=temperature,
            )
