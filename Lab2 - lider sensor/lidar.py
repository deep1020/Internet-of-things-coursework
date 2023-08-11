import serial, time, sys, RPi.GPIO as GPIO

red = 12
blue = 6

# led pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

ser = serial.Serial("/dev/ttyUSB1", 115200)

class RangeRead:
	def __init__(self):
		self.init()
		
	def init(self):
		ser.reset_input_buffer()
			
	def getTFminiData(self):
		while True:
			count = ser.in_waiting
			if count > 8:
				recv = ser.read(9)
				ser.reset_input_buffer()
				if recv[0] == 0X59 and recv[1] == 0X59:
					distance = int(recv[2]) + int(recv[3] << 8)
					print(distance, ' cm')
					time.sleep(0.5)
					if distance > 20:
						GPIO.output(blue, True)
						GPIO.output(red, False)
					else:
						GPIO.output(blue, False)
						GPIO.output(red, True)
						time.sleep(.5)
						GPIO.output(red, False)
						time.sleep(.5)
						GPIO.output(blue, False)
					
if __name__ == '__main__':
	try:
		if ser.is_open == False:
			ser.open()
		reader = RangeRead()
		reader.getTFminiData()
	except KeyboardInterrupt:
		if ser != None:
			ser.close()
		sys.exit()
