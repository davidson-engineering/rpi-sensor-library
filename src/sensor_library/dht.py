import logging
import adafruit_dht

logger = logging.getLogger(__name__)


class SensorDHT11:
    def __init__(self, pin, name: str = "DHT11"):
        self.name = name
        self.sensor = adafruit_dht.DHT11
        self.pin = pin

    def read(self):
        humidity, temperature = adafruit_dht.read(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            logger.info(
                "Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity)
            )
        else:
            logger.error("Sensor failure. Check wiring.")
            return None
        return dict(humidity=humidity, temperature=temperature)
