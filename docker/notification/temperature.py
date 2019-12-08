#!/usr/bin/python
import sys
import Adafruit_DHT
from pushbullet import Pushbullet

pb =Pushbullet (o.9bUaasge1wTDY2MMnonIjnAY9PunOZYO)

pin = 24
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
if humidity is not None and temperature is not None:
    print('{0:0.1f} {1:0.1f}'.format(temperature, humidity))
    push = pb.push_note("Test !", "Ca marche !")
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
