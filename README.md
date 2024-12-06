# hexagonal-ddd-in-python

This repository explains the hexagonal domain driven design approach in the Python language

## Exercise

Develop the core logic and adapters of a smart home system for temperature control. The architecture should include ports, services and adapters to ensure a flexible, modular application.

There should be a `TemperatureController`, where an interface can control the temperature by a given `thermostat_id` and a given `temperature`.
The `TemperatureController` should call a `TemperatureControlService` which should get a `ThermostatRepository`, which stores all `thermostats`.
A `Thermostat` contains it's `id` and which type it is accessable: via `UART` or via `API`.
Then there is a possibility to set the temperature of a thermostat via an `ApiThermostatAdapter` and via an `UartThermostatAdapter`.

Create a function to set all thermostats to 21 Celsius.
