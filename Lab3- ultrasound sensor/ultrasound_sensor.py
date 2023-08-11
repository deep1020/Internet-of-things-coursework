import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER=18
GPIO_ECHO=19


red = 12
blue = 6

# led pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

#
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distance():
	#set trigger to high
	GPIO.output(GPIO_TRIGGER,True)
	
	#set trigger after 0.01ms to low
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER,False)
	
	StartTime = time.time()
	StopTime = time.time()
	#save start time
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
		
	#save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
	
	#time difference between start an arrival
	TimeElapsed = StopTime - StartTime
	
	#multiply with sonic speed (34300cm/s)
	distance=(TimeElapsed * 34300)/2
	#and divide by 2 because there and back
	return distance
	
if __name__=='__main__':
	try:
		while True:
			#time.sleep(2)
			dist = distance()
			if dist > 30:
				GPIO.output(blue, True)
				GPIO.output(red, False)
			else:
				GPIO.output(blue, False)
				GPIO.output(red, True)
				time.sleep(.5)
				GPIO.output(red, False)
				time.sleep(.5)
				GPIO.output(blue, False)
			print("Measured Distance = %.1f cm" % dist)
			time.sleep(1)
			#reset by pressing ctrl+c
	except KeyboardInterrupt:
		print("Measurement stopped by user")
		GPIO.cleanup()
