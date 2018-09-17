# to run this script the following need to be added to: sudo crontab -e
# @reboot python /home/pi/ToolChangerForRobots/rebootUsingButton.py
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def Restart(channel):
	os.system("sudo shutdown -r now")

GPIO.add_event_detect(22, GPIO.FALLING, callback = Restart, bouncetime = 2000)

while 1:
	time.sleep(1)
