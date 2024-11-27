from decimal import Decimal
from pydantic import BaseModel

from core.domain.value_objects.temperature_scala import TemperatureScala


class Temperature(BaseModel):
    value: Decimal
    scala: TemperatureScala

    def to_fahrenheit(self) -> "Temperature":
        if self.scala == TemperatureScala.FAHRENHEIT:
            return self
        else:
            return Temperature(
                value=round(self.value * Decimal("1.8") + Decimal("32"), 1),
                scala=TemperatureScala.FAHRENHEIT,
            )

    def to_celsius(self) -> "Temperature":
        if self.scala == TemperatureScala.CELSIUS:
            return self
        else:
            return Temperature(
                value=round(
                    (self.value - Decimal("32")) * Decimal("5") / Decimal("9"),
                    1,
                ),
                scala=TemperatureScala.CELSIUS,
            )
