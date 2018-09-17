import io
import socket
import struct
from PIL import Image
import cv2
import numpy as np

# imageToolIP = '10.0.0.15'
# imageToolIP = '192.168.11.29'
imageToolIP = 'moisturepi'
moistureToolPort = 8001

def sendMoistureRequest():
    MESSAGE = "moistureReq"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((imageToolIP, moistureToolPort))
    s.send(MESSAGE)
    s.close()

def main():
    while True:
        raw_input("Hit any key for moisture request:")
        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('0.0.0.0', 8000))
        server_socket.listen(0)
        sendMoistureRequest()
        conn, addr = server_socket.accept()
        data = conn.recv(1024)
        conn.close()
        p_data = 100 - ((int(data)-523) * 100) / 500
        print(p_data)
        server_socket.close()


if __name__ == '__main__':
    main()