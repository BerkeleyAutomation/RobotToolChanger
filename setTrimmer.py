import socket
from PIL import Image
import numpy as np

cuttingToolIP = 'cuttingpi'
cuttingToolPort = 8003

def sendSpeedRequest(textToSend):
    BUFFER_SIZE = 1024
    # MESSAGE = "setSpeed_006_50_99"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((cuttingToolIP, cuttingToolPort))
    s.send(textToSend)
    s.close()

def main():
    while True:
        textToSend = raw_input("To set motor speed and direction enter: 'setSpeed_000_050':")
        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', 8000))
        server_socket.listen(0)
        sendSpeedRequest(textToSend)

if __name__ == '__main__':
    main()
