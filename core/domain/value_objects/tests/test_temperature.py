from decimal import Decimal
from core.domain.value_objects.temperature_scala import TemperatureScala
from core.domain.value_objects.temperature import Temperature


def test_temperature_fahrenheit_to_celsius():
    temperature = Temperature(
        value=Decimal(0),
        scala=TemperatureScala.FAHRENHEIT,
    )
    assert temperature.to_celsius() == Temperature(
        value=Decimal("-17.8"), scala=TemperatureScala.CELSIUS
    )


def test_temperature_celsius_to_fahrenheit():
    temperature = Temperature(
        value=Decimal(0),
        scala=TemperatureScala.CELSIUS,
    )
    assert temperature.to_fahrenheit() == Temperature(
        value=Decimal("32"), scala=TemperatureScala.FAHRENHEIT
    )
