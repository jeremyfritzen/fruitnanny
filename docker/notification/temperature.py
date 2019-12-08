#!/usr/bin/python
import sys
from board import 24
from pushbullet import Pushbullet

Pushbullet_API_key = ""
pin = 24

dht_device = adafruit_dht.DHT22(pin)
pb = Pushbullet(Pushbullet_API_key)

temperature = dht_device.temperature
humidity = dht_device.humidity