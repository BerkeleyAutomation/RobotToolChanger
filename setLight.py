import socket
import time

from PIL import Image
import numpy as np

# imageToolIP = '10.0.0.15'
#lightToolIP = '192.168.42.75'
lightToolIP = 'lightpi'
lightToolPort = 8003

def sendImageRequest(textToSend):
    BUFFER_SIZE = 1024
    # MESSAGE = "setLight_006_50_99"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((lightToolIP, lightToolPort))
    s.send(textToSend)
    s.close()

def main():
    while True:
        textToSend = raw_input("To set motor speed and direction enter: 'setLight_001_010_099':")
        sendImageRequest(textToSend)

if __name__ == '__main__':
    main()
