import RPi.GPIO as GPIO
import time

duty = 2

red = 12
blue = 6

GPIO_TRIGGER=18
GPIO_ECHO=19

GPIO.setmode(GPIO.BCM)
SERVO_PIN = 17
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo_motor = GPIO.PWM(SERVO_PIN, 50)


# led pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)


#sensor
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def rotate_clockwise():
	global duty
	#duty = 17
	servo_motor.start(duty)
	
	#while duty > 0:
	servo_motor.ChangeDutyCycle(duty)
	time.sleep(1)
	duty -= 1
	if(duty == 0):
		duty=100
		 
	return True


def rotate():	#counterclockwise
	global duty
	#duty = 2
	servo_motor.start(duty)
	time.sleep(1)
	
	#while duty <= 5:
	servo_motor.ChangeDutyCycle(duty)
	time.sleep(1)
	duty += 1
		
	if(duty == 100):
		duty=0
		
	return True


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

	#print("HEY")
		
	#save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
		
	#print("HEY2")
	
	#time difference between start an arrival
	TimeElapsed = StopTime - StartTime
	
	#print("HEY3")
	
	#multiply with sonic speed (34300cm/s)
	distance=(TimeElapsed * 34300)/2
	#and divide by 2 because there and back
	return distance


if __name__ == '__main__':
	try:
		while True:
			print('Rotate by 12 degree')
			#rotate()
	
			dist = distance()
			print("distance is " + str(dist))

			if dist > 30:
				GPIO.output(blue, True)
				GPIO.output(red, False)
				rotate()
			else:
				GPIO.output(blue, False)
				GPIO.output(red, True)
				time.sleep(.5)
				GPIO.output(red, False)
				time.sleep(.5)
				GPIO.output(blue, False)
				rotate_clockwise()
	
			time.sleep(1)
	except KeyboardInterrupt:
			servo_motor.stop()
			GPIO.cleanup()	
	
