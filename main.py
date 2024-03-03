#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Matthew Davidson
# Created Date: 2023-01-23
# version ='1.0'
# ---------------------------------------------------------------------------
"""Demonstration code for the DHT11 sensor."""
# ---------------------------------------------------------------------------

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
