# Importing modules
import spidev # To communicate with SPI devices
import sys
import math
from numpy import interp	# To scale values
from time import sleep	# To add delay
import RPi.GPIO as GPIO	# To use GPIO pins
# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)
# Initializing LED pin as OUTPUT pin
# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
smallcounter = 0
while True:
	output = analogInput(0) # Reading from CH0
	output = interp(output, [0, 1023], [0, 100])
	output = output * 3.3 / 100
	output = (133.42*output*output*output - 255.86*output*output + 857.39*output)/2 # calculations from GravityTDS library
	print(str(math.trunc(output)) + " ppm")
  	sleep(0.1)
