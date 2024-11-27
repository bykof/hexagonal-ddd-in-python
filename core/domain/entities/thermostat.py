from pydantic import BaseModel

from core.domain.value_objects.thermostat_port_type import ThermostatPortType


class Thermostat(BaseModel):
    id: str
    port_type: ThermostatPortType
