import logging
import adafruit_dht
import board

logger = logging.getLogger(__name__)

from sensor_library.sensor import Sensor


class SensorDHT11(Sensor):
    def __init__(self, pin: adafruit_dht.Pin, name: str = "DHT11"):
        self.name = name
        if isinstance(pin, int):
            pin = getattr(board, f"D{pin}")
        elif isinstance(pin, str):
            pin = getattr(board, pin)
        self.sensor = adafruit_dht.DHT11(pin)

    def measure(self) -> dict:
        try:
            humidity, temperature = self.sensor.humidity, self.sensor.temperature
        except RuntimeError as error:
            logger.error(f"RuntimeError reading sensor. {error} Continuing ... ")

        if humidity is not None and temperature is not None:
            logger.info(
                "Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity)
            )
        else:
            logger.error("Sensor failure. Check wiring.")
            return None
        return dict(humidity=humidity, temperature=temperature)
