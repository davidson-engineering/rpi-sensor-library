# rpi-sensor-library
### A library for interfacing with sensors on the Raspberry Pi platform

```python
import time
import logging

from sensor_library.dht import SensorDHT11

logger = logging.getLogger(__name__)

SENSOR_PIN = 18


def read_sensor():
    sensor = SensorDHT11(pin=SENSOR_PIN)

    while True:
        print(sensor.read())

        time.sleep(1)


if __name__ == "__main__":
    read_sensor()
```
