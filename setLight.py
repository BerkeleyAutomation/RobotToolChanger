import socket
from PIL import Image
import numpy as np

# imageToolIP = '10.0.0.15'
lightToolIP = '192.168.42.75'
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
        textToSend = raw_input("Hit any key for image request:")
        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', 8000))
        server_socket.listen(0)
        sendImageRequest(textToSend)

if __name__ == '__main__':
    main()
