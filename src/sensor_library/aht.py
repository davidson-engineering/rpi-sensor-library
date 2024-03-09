import logging
import adafruit_ahtx0
import board

logger = logging.getLogger(__name__)

from sensor_library.sensor import Sensor


class SensorAHT20(Sensor):
    def __init__(self):
        self.sensor = adafruit_ahtx0.AHTx0(board.I2C())

    def measure(self) -> dict:
        try:
            humidity, temperature = (
                self.sensor.relative_humidity,
                self.sensor.temperature,
            )
        except RuntimeError as error:
            logger.error(f"RuntimeError reading sensor. {error} Continuing ... ")

        if humidity is not None and temperature is not None:
            logger.debug(
                "Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity)
            )
            return dict(humidity=humidity, temperature=temperature)
        else:
            logger.error("Sensor failure. Check wiring.")
            return

    def print(self):
        print(f"Temperature {self.sensor.temperature:.2f} {chr(176)}C")
        print(f"Humidity {self.sensor.relative_humidity:2f}%")
