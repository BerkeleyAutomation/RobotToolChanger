import socket
import io
import struct
import time
import picamera
import threading
import sys
import RPi.GPIO as GPIO
#import Adafruit_MCP3008

LED_STATE=0 #0-waiting consnt; 1-sending moisture

def controlLED():
	global LED_STATE
	#LED_STATE = 0
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
		while LED_STATE==0: LED_blink(bluePin,0.8)
		LED_close(greenPin, bluePin, redPin)
		while LED_STATE==1: LED_const(greenPin)
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

#def MoistureValue():
#    CLK = 4
#    MISO = 17
#    MOSI = 27
#    CS = 22
#    mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
#
#    Mvalue = mcp.read_adc(0)
#    print(Mvalue)
#    return Mvalue

def getLocalMoistureData():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(("127.0.0.1", 8008))
	data, _ = s.recvfrom(10)
	s.close()
	return data

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
					if data == 'moistureReq':
						LED_STATE=1
						#data = MoistureValue()
						data = getLocalMoistureData()
						#print(moistureData)
						s_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s_send.connect((addr[0], 8000))
						s_send.send(str(data))
						s_send.close()
						#conn.sendall('rtk')
				#conn.close()
		except:
			pass
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
