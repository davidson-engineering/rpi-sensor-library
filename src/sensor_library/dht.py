import logging
import adafruit_dht

logger = logging.getLogger(__name__)


class SensorDHT11:
    def __init__(self, pin, name: str = "DHT11"):
        self.name = name
        self.pin = pin
        self.sensor = adafruit_dht.DHT11(pin=pin)

    def measure(self):
        self.sensor.measure()
        humidity, temperature = self.sensor.humidity, self.sensor.temperature
        if humidity is not None and temperature is not None:
            logger.info(
                "Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity)
            )
        else:
            logger.error("Sensor failure. Check wiring.")
            return None
        return dict(humidity=humidity, temperature=temperature)
