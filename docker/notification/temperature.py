#!/usr/bin/python

import time
import adafruit_dht
import board
from pushbullet import Pushbullet

dhtDevice = adafruit_dht.DHT22(board.D24)
pb = Pushbullet("")

temp_min = 18
temp_max = 20
frequence_notification = 1200
monitor_url = "http://rpi-nanny.home/"

while True:
	try:
		# Print the values to the serial port
		temperature_c = dhtDevice.temperature
		message = ("Rpi-Nanny : {}°C !".format(temperature_c))
		print(message)
		if temperature_c > temp_max or temperature_c < temp_min :
			#push = pb.push_note("Rpi-Nanny", message)
			push = pb.push_link(message, monitor_url)
			time.sleep(frequence_notification)
	except RuntimeError as error:
		# Errors happen fairly often, DHT's are hard to read, just keep going
		print(error.args[0])

	time.sleep(5.0)

# Print the values to the serial port
#print(message)
