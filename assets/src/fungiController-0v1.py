import board
import adafruit_am2320
from w1thermsensor import W1ThermSensor, Sensor
import psychrolib
import digitalio
from time import sleep

rHSetPoint = 90 #%
controlPeriod = 30 #seconds

#environment
psychrolib.SetUnitSystem(psychrolib.SI)
altitude = 208 #meters
pressure = psychrolib.GetStandardAtmPressure(altitude)

# calibration: actual value = measured + offset
offsetDryT = 0.7
offsetWetT = 0.4

def setup():
	# humidity sensor
	i2c = board.I2C()
	am = adafruit_am2320.AM2320(i2c)

	# temperature sensors
	dryTId = '00000d1348e5'
	wetTId = '00000cb1b969'
	dryTSensor = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id = dryTId)
	wetTSensor = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id = wetTId)

	# relays
	waterHeater = digitalio.DigitalInOut(board.D17)
	waterHeater.direction = digitalio.Direction.OUTPUT
	waterHeater.value = True #active low

	return dryTSensor, wetTSensor, am, waterHeater


def printAll(dryT, wetT, internalRH, internalT, calcRH):
	print('-------------------------------------------')
	print(f'Dry air temperature:\t{dryT:.1f}')
	print(f'Wet air temperature:\t{wetT:.1f}')
	print(f'Calculated intake humidity:\t{calcRH:.1f}')
	print(f'Measured internal humidity:\t{internalRH}')
	print(f'Measured internal temperature:\t{internalT}')


def update(dryT, dryTSensor, wetT, wetTSensor, internalRH, internalT, am, calcRH):
	dryT = dryTSensor.get_temperature() + offsetDryT
	wetT = wetTSensor.get_temperature() + offsetWetT
	internalRH = am.relative_humidity
	internalT = am.temperature
	try:
		calcRH = psychrolib.GetRelHumFromTWetBulb(dryT, wetT, pressure) * 100
	except(ValueError): #above 100% humidity
		reversed = psychrolib.GetRelHumFromTWetBulb(wetT, dryT, pressure) * 100
		calcRH = 200 - reversed

	return(dryT, wetT, internalRH, internalT, calcRH)


def adjust(internalRH, waterHeater):
	if internalRH < rHSetPoint:
		waterHeater.value = False #ON
		print('Water heater ON.')
	else:
		waterHeater.value = True #OFF
		print('Water heater OFF.')


def main():
	dryT = 0.0
	wetT = 0.0
	internalRH = 0.0
	internalT = 0.0
	calcRH = 0.0

	dryTSensor, wetTSensor, am, waterHeater = setup()

	while(True):
		dryT, wetT, internalRH, internalT, calcRH= update(dryT, dryTSensor, wetT, wetTSensor, internalRH, internalT, am, calcRH)
		adjust(internalRH, waterHeater)
		printAll(dryT, wetT, internalRH, internalT, calcRH)
		sleep(controlPeriod)


if __name__ == '__main__':
	main()
