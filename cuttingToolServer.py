import socket
import io
import struct
import time
import threading
import sys
import RPi.GPIO as GPIO
import numpy as np

LED_STATE=0 #0-waiting consnt; 1-sending image

LED1 = 100
LED2 = 100
LED3 = 100

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
	global LED1, LED2, LED3

	#data = 'setSpeed_005'

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
							LED1 = np.int(data[9:12])
							LED2 = np.int(data[13:16])
							LED3 = np.int(data[17:20])
							print(LED1, LED2, LED3)
							time.sleep(0.1)
						except:
							LED_STATE = 0
							LED1 = 0
							LED2 = 0
							LED3 = 0
							print('String format error. Currect format is: setLight_004_050_100')
							time.sleep(0.1)
				conn.close()
		except:
			print('error')


def main(args):
	global LED_STATE
	global LED1, LED2, LED3

	LED_STATE = 0
	LED1 = 0
	LED2 = 0
	LED3 = 0

	LED1Pin = 35
	LED2Pin = 33
	LED3Pin = 12

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LED1Pin, GPIO.OUT)
	GPIO.setup(LED2Pin, GPIO.OUT)
	GPIO.setup(LED3Pin, GPIO.OUT)

	LED1Ctl = GPIO.PWM(LED1Pin, 100)
	LED2Ctl = GPIO.PWM(LED2Pin, 100)
	LED3Ctl = GPIO.PWM(LED3Pin, 100)

	LED1Ctl.start(LED1)
	LED2Ctl.start(LED2)
	LED3Ctl.start(LED3)
	
	LED1Ctl.ChangeDutyCycle(0)
	LED2Ctl.ChangeDutyCycle(0)
	LED3Ctl.ChangeDutyCycle(0)
	time.sleep(0.05)


	control_LED_thread = threading.Thread(target=controlLED)
	control_LED_thread.start()

	wait_for_string_thread = threading.Thread(target=waitForString)
	wait_for_string_thread.start()

	while True:
		LED1Ctl.ChangeDutyCycle(LED1)
		LED2Ctl.ChangeDutyCycle(LED2)
		LED3Ctl.ChangeDutyCycle(LED3)
		time.sleep(0.05)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
