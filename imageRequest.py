import io
import socket
import struct
from PIL import Image
import cv2
import numpy as np

# imageToolIP = '10.0.0.15'
# imageToolIP = '192.168.11.29'
imageToolIP = 'camerapi'
imageToolPort = 8001

def sendImageRequest():
    BUFFER_SIZE = 1024
    MESSAGE = "imageReq"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((imageToolIP, imageToolPort))
    s.send(MESSAGE)
    s.close()

def receivingImage(server_socket):
    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('rb')

    try:
        while True:
            # Read the length of the image as a 32-bit unsigned int. If the
            # length is zero, quit the loop

            image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
            if not image_len:
                break
            # Construct a stream to hold the image data and read the image
            # data from the connection

            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))
            # Rewind the stream, open it as an image with PIL and do some
            # processing on it
            image_stream.seek(0)
            image = Image.open(image_stream)
            image.save('Desktop/1.jpg')
            print('Image is %dx%d' % image.size)
            image.verify()
            im = np.array(image)
            connection.close()
            return im
    except:
        print('rtk')
        pass

def main():
    while True:
        raw_input("Hit any key for image request:")
        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', 8000))
        server_socket.listen(0)
        sendImageRequest()
        im = receivingImage(server_socket)
        server_socket.close()
        cv2.imshow('rtk', im)
        cv2.waitKey(2000)
if __name__ == '__main__':
    main()
