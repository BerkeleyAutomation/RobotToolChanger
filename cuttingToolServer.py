import socket
import io
import struct
import time
import threading
import sys
import RPi.GPIO as GPIO
import numpy as np

LED_STATE=0 #0-waiting consnt; 1-sending image
motorSpeed = 0
motorDir = 0

def controlLED():
	global LED_STATE
	LED_STATE = 0
	redPin = 40
	greenPin = 32
	bluePin = 36
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(redPin, GPIO.OUT)
	GPIO.setup(greenPin, GPIO.OUT)
	GPIO.setup(bluePin, GPIO.OUT)
	
	LED_close(greenPin, bluePin, redPin)
	while True:
		print(LED_STATE)
		while LED_STATE==0: LED_blink(greenPin,0.8)

		LED_close(greenPin, bluePin, redPin)
		
		while LED_STATE==1: LED_const(bluePin)

		LED_close(greenPin, bluePin, redPin)
		
def LED_blink(pin,sleepTime):
	GPIO.output(pin, GPIO.LOW)
	time.sleep(sleepTime)
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(sleepTime)

def LED_close(greenPin, bluePin, redPin):
	GPIO.output(greenPin, GPIO.HIGH)
	GPIO.output(bluePin, GPIO.HIGH)
	GPIO.output(redPin, GPIO.HIGH)

def LED_const(pin):
	GPIO.output(pin, GPIO.LOW)

def waitForString():
	global LED_STATE
	global motorSpeed
	global motorDir
	#data = 'setSpeed_000_040' first arg is motor direction (000-->CW, 001-->CCW) second arg is motor speed

	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind(('0.0.0.0', 8003))
			
			LED_STATE = 0
			while True:
				LED_STATE = 0
				s.listen(1)
				conn, addr = s.accept()
				print 'connection address:', addr
				while True:
					data = conn.recv(1024)
					if not data: break

					if data[0:8] == 'setSpeed':
						try:
							LED_STATE = 1
							motorDir = np.int(data[9:12])
							motorSpeed = np.int(data[13:16])
							print(motorDir, motorSpeed)
							time.sleep(0.1)
						except:
							LED_STATE = 0
							motorDir = 0
							motorSpeed = 0
							print('String format error. Currect format is: setSpeed_000_045')
							time.sleep(0.1)
				conn.close()
		except:
			print('error')


def main(args):
	global LED_STATE
	global motorSpeed
	global motorDir

	LED_STATE = 0
	motorSpeed = 0
	motorDir = 0

	motorPWMPin = 35
	motorDir1Pin = 31
	motorDir2Pin = 29

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(motorPWMPin, GPIO.OUT)
	GPIO.setup(motorDir1Pin, GPIO.OUT)
	GPIO.setup(motorDir2Pin, GPIO.OUT)

	#set dir
	GPIO.output(motorDir1Pin, GPIO.HIGH)
	GPIO.output(motorDir2Pin, GPIO.LOW)

	#set freq
	motorCtl = GPIO.PWM(motorPWMPin, 100)

	#set initial speed
	motorCtl.start(motorSpeed)

	time.sleep(0.05)

	control_LED_thread = threading.Thread(target=controlLED)
	control_LED_thread.start()

	wait_for_string_thread = threading.Thread(target=waitForString)
	wait_for_string_thread.start()

	while True:
		motorCtl.ChangeDutyCycle(10)

		if motorDir==0:
			GPIO.output(motorDir1Pin, GPIO.HIGH)
			GPIO.output(motorDir2Pin, GPIO.LOW)
		else:
			GPIO.output(motorDir1Pin, GPIO.LOW)
			GPIO.output(motorDir2Pin, GPIO.HIGH)

		time.sleep(0.05)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
