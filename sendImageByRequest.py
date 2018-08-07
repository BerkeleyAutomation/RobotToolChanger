import socket
import io
import struct
import time
import picamera
import threading
import sys
import RPi.GPIO as GPIO

LED_STATE=0 #0-waiting consnt; 1-sending image

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
		while LED_STATE==0: LED_blink(greenPin, 0.8)
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

def sendImage():
	client_socket = socket.socket()
	#client_socket.connect(('10.0.0.21',8000)) #automation
	#client_socket.connect(('192.168.11.7',8000)) #bufolo
	client_socket.connect(('dell',8000)) #hostname
	connection = client_socket.makefile('wb')
	try:
		with picamera.PiCamera() as camera:
			#camera.resolution= (640, 480)
			#camera.start_preview()
			time.sleep(1)
			stream = io.BytesIO()
			camera.capture(stream, 'jpeg')
			connection.write(struct.pack('<L', stream.tell()))
			connection.flush()
			stream.seek(0)
			connection.write(stream.read())
			stream.seek(0)
			stream.truncate()
		connection.write(struct.pack('<L',0))
		connection.close()
		client_socket.close()
	except:
		pass
	
def main(args):
	global LED_STATE
	LED_thread = threading.Thread(target=controlLED)
	LED_thread.start()
	LED_STATE=0
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind(('0.0.0.0',8001))
			LED_STATE=0
			while True:
				LED_STATE=0
				s.listen(1)
				conn, addr = s.accept()
				print 'connection address:', addr
				while 1:
					data = conn.recv(1024)
					if not data: break
					print data
					if data == 'imageReq':
						LED_STATE=1
						sendImage()
				#conn.close()
		except:
			pass
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
