#!/usr/bin/python
import time
import adafruit_dht
import board
from pushbullet import Pushbullet

dhtDevice = adafruit_dht.DHT22(board.D24)
pb = Pushbullet("")

temp_min = 18
temp_max = 21

while True:
	try:
		# Print the values to the serial port
		temperature_c = dhtDevice.temperature
		message = ("La température est de {}".format(temperature_c))
		if temperature_c > temp_max or temperature_c < temp_min :
			push = pb.push_note("Rpi-Nanny", message)
			print(message)
	except RuntimeError as error:
		# Errors happen fairly often, DHT's are hard to read, just keep going
		print(error.args[0])

	time.sleep(5.0)

# Print the values to the serial port
#print(message)
