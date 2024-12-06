from adapters.api_thermostat_adapter import ApiThermostatAdapter
from adapters.uart_thermostat_adapter import UartThermostatAdapter
from controllers.thermostat_controller import ThermostatController
from core.domain.entities.thermostat import Thermostat
from core.domain.value_objects.thermostat_port_type import ThermostatPortType
from core.ports.temperature_control_port import TemperatureControlPort
from core.ports.thermostat_port import ThermostatPort
from core.ports.thermostat_repository import ThermostatRepository
from core.services.temperature_control_service import TemperatureControlService


def main(
    thermostat_controller: ThermostatController,
    thermostat_repository: ThermostatRepository,
):
    for thermostat in thermostat_repository.get_all():
        thermostat_controller.update_temperature_of_thermostat_id(
            thermostat_id=thermostat.id, temperature=21
        )


if __name__ == "__main__":
    thermostat_repository: ThermostatRepository = ThermostatRepository()
    api_thermostat_adapter: ThermostatPort = ApiThermostatAdapter()
    uart_thermostat_adapter: ThermostatPort = UartThermostatAdapter()
    temperature_control_port: TemperatureControlPort = TemperatureControlService(
        thermostat_ports=[api_thermostat_adapter, uart_thermostat_adapter]
    )
    thermostat_repository.add(
        [
            Thermostat(id=1, port_type=ThermostatPortType.API),
            Thermostat(id=2, port_type=ThermostatPortType.UART),
        ]
    )
    thermostat_controller = ThermostatController(
        temperature_control_port=temperature_control_port,
        thermostat_repository=thermostat_repository,
    )

    main(
        thermostat_controller=thermostat_controller,
        thermostat_repository=thermostat_repository,
    )
