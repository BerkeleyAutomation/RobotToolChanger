import math
from time import sleep

import tf
from autolab_core import RigidTransform
from yumipy import YuMiRobot
import sys

import io
import socket
import struct
from PIL import Image
import cv2
import numpy as np

yumi = YuMiRobot()


def move_YUMI(X, Y, H, ROT0, ROT1, ROT2, V, robot_side):
    pos = RigidTransform()
    pos.from_frame = 'robot'

    pos.translation = X, Y, H
    quat = tf.transformations.quaternion_from_euler(math.radians(ROT0), math.radians(ROT1), math.radians(ROT2))
    pos.quaternion[0:3] = quat[0:3]
    pos.rotation = RigidTransform.rotation_from_quaternion(quat)
    yumi.set_v(V)
    if robot_side == 'r':
        yumi.right.goto_pose(pos)
    elif robot_side == 'l':
        yumi.left.goto_pose(pos)
    else:
        pass
    # sleep(.1)


def light_tool(state, robot_side):
    if state == 'connect':
        v_very_slow = 50
        v_slow = 100
        v = 200

        h0 = 0.1453
        h1 = 0.093

        x0 = 0.394  # y = -0.4303
        x1 = 0.4967  # y = -0.4324
        x2 = 0.5525  # y = -0.4332
        x3 = x2
        x4 = 0.45  # 0.4949  # y = -0.4353
        x5 = 0.394

        y = -0.436

        rot0_0 = 180
        rot0_1 = 155

        rot1_0 = 0
        rot1_1 = -2

        rot2 = 180

        move_YUMI(x0, y, h0, rot0_0, rot1_0, rot2, v, robot_side)  # start point
        move_YUMI(x1, y, h0, rot0_0, rot1_0, rot2, v_slow, robot_side)  # point 1
        move_YUMI(x2, y, h0, rot0_1, rot1_0, rot2, v_very_slow, robot_side)
        move_YUMI(x3, y, h1, rot0_1, rot1_0, rot2, v_slow, robot_side)

        x_tmp = x3
        rot_tmp = -2.5
        for i in range(0, 22, 1):
            x_tmp = x_tmp - 0.0017
            rot_tmp = -rot_tmp
            move_YUMI(x_tmp, y, h1, rot0_1 + rot_tmp, rot1_0, rot2, 1000, robot_side)

        move_YUMI(x5, y, h1, rot0_1, rot1_0, rot2, v, robot_side)

    elif state == 'disconnect':
        v_very_slow = 50
        v_slow = 100
        v = 200

        # Disconnect tool parameters
        h0 = 0.1453
        h1 = 0.095

        x0 = 0.394  # y = -0.4303
        x1 = 0.4967  # y = -0.4324
        x2 = 0.5533  # y = -0.4332
        x3 = x2
        x4 = 0.495  # y = -0.4353
        x5 = 0.49
        x6 = 0.395

        y = -0.4365

        rot0_0 = 180
        rot0_1 = 155

        rot1_0 = 0
        rot1_1 = 2

        rot2 = 180

        move_YUMI(x6, y, h1, rot0_1, rot1_1, rot2, v, robot_side)
        move_YUMI(x5, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.005, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.01, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.015, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x3, y, h1, rot0_1, rot1_0, rot2, v_very_slow, robot_side)
        move_YUMI(x2, y, h0, rot0_1, rot1_0, rot2, v_slow, robot_side)
        move_YUMI(x1, y, h0, rot0_1, rot1_0, rot2, v_slow, robot_side)
        move_YUMI(x0, y, h0, rot0_1, rot1_0, rot2, v, robot_side)
    else:
        pass


def moisture_tool(state, robot_side):
    if state == 'connect':
        v_very_slow = 50
        v_slow = 100
        v = 200

        h0 = 0.1453 + 0.131
        h1 = 0.093 + 0.131

        x0 = 0.394 + 0.052  # y = -0.4303
        x1 = 0.4967 + 0.052  # y = -0.4324
        x2 = 0.5525 + 0.052  # y = -0.4332
        x3 = x2
        x4 = 0.45 + 0.052  # 0.4949  # y = -0.4353
        x5 = 0.394 + 0.052

        y = -0.318

        rot0_0 = 180
        rot0_1 = 155

        rot1_0 = 0
        rot1_1 = -2

        rot2 = 180

        move_YUMI(x0, y, h0, rot0_0, rot1_0, rot2, v, robot_side)  # start point
        move_YUMI(x1, y, h0, rot0_0, rot1_0, rot2, v_slow, robot_side)  # point 1
        move_YUMI(x2, y, h0, rot0_1, rot1_0, rot2, v_very_slow, robot_side)
        move_YUMI(x3, y, h1, rot0_1, rot1_0, rot2, v_slow, robot_side)

        x_tmp = x3
        rot_tmp = -2.5
        for i in range(0, 22, 1):
            x_tmp = x_tmp - 0.0017
            rot_tmp = -rot_tmp
            move_YUMI(x_tmp, y, h1, rot0_1 + rot_tmp, rot1_0, rot2, 1000, robot_side)

        move_YUMI(x5, y, h1, rot0_1, rot1_0, rot2, v, robot_side)
    elif state == 'disconnect':
        v_very_slow = 50
        v_slow = 100
        v = 200

        # Disconnect tool parameters
        h0 = 0.1453 + 0.131
        h1 = 0.093 + 0.131

        x0 = 0.394 + 0.052  # y = -0.4303
        x1 = 0.4967 + 0.052  # y = -0.4324
        x2 = 0.5533 + 0.052  # y = -0.4332
        x3 = x2
        x4 = 0.495 + 0.052  # y = -0.4353
        x5 = 0.49 + 0.052
        x6 = 0.395 + 0.052

        y = -0.318

        rot0_0 = 180
        rot0_1 = 155

        rot1_0 = 0
        rot1_1 = 2

        rot2 = 180

        move_YUMI(x6, y, h1, rot0_1, rot1_1, rot2, v, robot_side)
        move_YUMI(x5, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.005, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.01, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.015, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x3, y, h1, rot0_1, rot1_0, rot2, v_very_slow, robot_side)
        move_YUMI(x2, y, h0, rot0_1, rot1_0, rot2, v_slow, robot_side)
        move_YUMI(x1, y, h0, rot0_1, rot1_0, rot2, v_slow, robot_side)
        move_YUMI(x0, y, h0, rot0_1, rot1_0, rot2, v, robot_side)

    else:
        pass


def cutting_tool(state, robot_side):
    if state == 'connect':
        v_very_slow = 50
        v_slow = 100
        v = 200

        h0 = 0.1453 + 0.131
        h1 = 0.093 + 0.131 - 0.003

        x0 = 0.394 + 0.052  # y = -0.4303
        x1 = 0.4967 + 0.052  # y = -0.4324
        x2 = 0.5525 + 0.052  # y = -0.4332
        x3 = x2
        x4 = 0.45 + 0.052  # 0.4949  # y = -0.4353
        x5 = 0.394 + 0.052

        y = 0.31

        rot0_0 = 180
        rot0_1 = 155

        rot1_0 = 0
        rot1_1 = -3

        rot2 = 180

        move_YUMI(x0, y, h0, rot0_0, rot1_0, rot2, v, robot_side)  # start point
        move_YUMI(x1, y, h0, rot0_0, rot1_0, rot2, v_slow, robot_side)  # point 1
        move_YUMI(x2, y, h0, rot0_1, rot1_0, rot2, v_very_slow, robot_side)
        move_YUMI(x3, y, h1, rot0_1, rot1_0, rot2, v_slow, robot_side)

        x_tmp = x3
        rot_tmp = -1.5
        for i in range(0, 30, 1):
            x_tmp = x_tmp - 0.0012
            rot_tmp = -rot_tmp
            move_YUMI(x_tmp, y, h1, rot0_1 + rot_tmp, rot1_0, rot2, 1000, robot_side)

        move_YUMI(x5, y, h1, rot0_1, rot1_0, rot2, v, robot_side)
    elif state == 'disconnect':
        v_very_slow = 50
        v_slow = 100
        v = 200

        # Disconnect tool parameters
        h0 = 0.1453 + 0.131
        h1 = 0.093 + 0.131 - 0.003

        x0 = 0.394 + 0.052  # y = -0.4303
        x1 = 0.4967 + 0.052  # y = -0.4324
        x2 = 0.5533 + 0.052  # y = -0.4332
        x3 = x2
        x4 = 0.495 + 0.052  # y = -0.4353
        x5 = 0.49 + 0.052
        x6 = 0.395 + 0.052

        y = 0.31

        rot0_0 = 180
        rot0_1 = 155

        rot1_0 = 0
        rot1_1 = 2

        rot2 = 180

        move_YUMI(x6, y, h1, rot0_1, rot1_1, rot2, v, robot_side)
        move_YUMI(x5, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.005, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.01, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.015, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x3, y, h1, rot0_1, rot1_0, rot2, v_very_slow, robot_side)
        move_YUMI(x2, y, h0, rot0_1, rot1_0, rot2, v_slow, robot_side)
        move_YUMI(x1, y, h0, rot0_1, rot1_0, rot2, v_slow, robot_side)
        move_YUMI(x0, y, h0, rot0_1, rot1_0, rot2, v, robot_side)

    else:
        pass


def camera_tool(state, robot_side):
    if state == 'connect':
        v_very_slow = 50
        v_slow = 100
        v = 200

        h0 = 0.1453
        h1 = 0.092

        x0 = 0.394  # y = -0.4303
        x1 = 0.4967  # y = -0.4324
        x2 = 0.5525  # y = -0.4332
        x3 = x2
        x4 = 0.45  # 0.4949  # y = -0.4353
        x5 = 0.394

        y = 0.43

        rot0_0 = 180
        rot0_1 = 155

        rot1_0 = 0
        rot1_1 = -2

        rot2 = 180

        move_YUMI(x0, y, h0, rot0_0, rot1_0, rot2, v, robot_side)  # start point
        move_YUMI(x1, y, h0, rot0_0, rot1_0, rot2, v_slow, robot_side)  # point 1
        move_YUMI(x2, y, h0, rot0_1, rot1_0, rot2, v_very_slow, robot_side)
        move_YUMI(x3, y, h1, rot0_1, rot1_0, rot2, v_slow, robot_side)

        x_tmp = x3
        rot_tmp = -1.5
        for i in range(0, 30, 1):
            x_tmp = x_tmp - 0.0012
            rot_tmp = -rot_tmp
            move_YUMI(x_tmp, y, h1, rot0_1 + rot_tmp, rot1_0, rot2, 1000, robot_side)

        move_YUMI(x5, y, h1, rot0_1, rot1_0, rot2, v, robot_side)

    elif state == 'disconnect':
        v_very_slow = 50
        v_slow = 100
        v = 200

        # Disconnect tool parameters
        h0 = 0.1453
        h1 = 0.093

        x0 = 0.394  # y = -0.4303
        x1 = 0.4967  # y = -0.4324
        x2 = 0.5533  # y = -0.4332
        x3 = x2
        x4 = 0.495  # y = -0.4353
        x5 = 0.49
        x6 = 0.395

        y = 0.43

        rot0_0 = 180
        rot0_1 = 155

        rot1_0 = 0
        rot1_1 = 2

        rot2 = 180

        move_YUMI(x6, y, h1, rot0_1, rot1_1, rot2, v, robot_side)
        move_YUMI(x5, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.005, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.01, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x5 + 0.015, y, h1, rot0_1, rot1_1, rot2, v_very_slow, robot_side)
        move_YUMI(x3, y, h1, rot0_1, rot1_0, rot2, v_very_slow, robot_side)
        move_YUMI(x2, y, h0, rot0_1, rot1_0, rot2, v_slow, robot_side)
        move_YUMI(x1, y, h0, rot0_1, rot1_0, rot2, v_slow, robot_side)
        move_YUMI(x0, y, h0, rot0_1, rot1_0, rot2, v, robot_side)
    else:
        pass


def getImage(im_name):
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(0)

    MESSAGE = "imageReq"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('camerapi', 8001))
    s.send(MESSAGE)
    s.close()

    im = receivingImage(server_socket)
    server_socket.close()
    cv2.imshow('rtk', im)
    cv2.waitKey(1000)
    cv2.imwrite('/home/ron/remoteComputer/data/' + str(im_name) + '.jpg', im)


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
            image.save('/home/ron/Desktop/1.jpg')
            print('Image is %dx%d' % image.size)
            image.verify()
            im = np.array(image)
            connection.close()
            return im
    except:
        print('rtk')
        pass

def setLight(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('lightpi', 8003))
    s.send(msg)
    s.close()
def cameraAndLight():
    image_num=1
    light_tool('connect', 'r')
    camera_tool('connect', 'l')
    sleep(90)
    setLight('setLight_020_050_020')
    sleep(1)

    # move to initial position

    zR = 0.2
    rotR_1 = 155
    rotR_2 = 30
    rotR_3 = 200

    zL = 0.21
    rotL_1 = 155
    rotL_2 = 0
    rotL_3 = 180


    x = 0.44
    y = 0.1
    move_YUMI(x, y, zL, rotL_1, rotL_2, rotL_3, 200, 'l')
    move_YUMI(x - 0.1, y - 0.1, zR, rotR_1, rotR_2, rotR_3, 200, 'r')
    sleep(1)
    getImage(image_num)
    image_num=image_num+1
    sleep(1)
    for h in range(0,2,1):
        y = y - 0.1
        move_YUMI(x - 0.1, y - 0.1,   zR, rotR_1, rotR_2, rotR_3, 200, 'r')
        move_YUMI(x,    y,          zL, rotL_1, rotL_2, rotL_3, 200, 'l')
        sleep(1)
        getImage(image_num)
        image_num = image_num + 1
        sleep(1)

    x = x + 0.1
    y = 0.1
    move_YUMI(x, y, 0.25, rotL_1, rotL_2, rotL_3, 200, 'l')
    move_YUMI(x - 0.1, y - 0.1, zR, rotR_1, rotR_2, rotR_3, 200, 'r')
    sleep(1)
    getImage(image_num)
    image_num = image_num + 1
    sleep(1)
    for h in range(0, 2, 1):
        y = y - 0.1
        move_YUMI(x - 0.1, y - 0.1, zR, rotR_1, rotR_2, rotR_3, 200, 'r')
        move_YUMI(x, y, 0.25, rotL_1, rotL_2, rotL_3, 200, 'l')
        sleep(1)
        getImage(image_num)
        image_num = image_num + 1
        sleep(1)

    xR = x
    x = x + 0.1
    y = 0.1
    move_YUMI(x, y, 0.25, rotL_1, rotL_2, rotL_3, 200, 'l')
    move_YUMI(xR - 0.1, y - 0.1, zR, rotR_1, rotR_2, rotR_3, 200, 'r')
    sleep(1)
    getImage(image_num)
    image_num = image_num + 1
    sleep(1)
    for h in range(0, 2, 1):
        y = y - 0.1
        move_YUMI(xR - 0.1, y - 0.1, zR, rotR_1, rotR_2, rotR_3, 200, 'r')
        move_YUMI(x, y, 0.25, rotL_1, rotL_2, rotL_3, 200, 'l')
        sleep(1)
        getImage(image_num)
        image_num = image_num + 1
        sleep(1)
        
    armIntPos('l')
    armIntPos('r')
    setLight('setLight_000_000_000')
    light_tool('disconnect', 'r')
    camera_tool('disconnect', 'l')


def armIntPos(robot_side):
    if robot_side == 'r':
        move_YUMI(0.42, -0.1, 0.22, 155, 0, 180, 200, 'r')
    elif robot_side == 'l':
        move_YUMI(0.42, 0.1, 0.22, 155, 0, 180, 200, 'l')
    else:
        pass


def main():
    if len(sys.argv) > 1:
        loop = int(sys.argv[1])
    else:
        loop = 1
    armIntPos('l')
    armIntPos('r')

    sleep(1)
    cameraAndLight()
    # itr = 0
    # for i in range(0,loop,1):
    #     print('iteration: ', itr)
    #     light_tool('connect', 'r')
    #     light_tool('disconnect', 'r')
    #     moisture_tool('connect', 'r')
    #     moisture_tool('disconnect', 'r')
    #     cutting_tool('connect', 'l')
    #     cutting_tool('disconnect', 'l')
    #     camera_tool('connect', 'l')
    #     camera_tool('disconnect', 'l')
    #     itr = itr + 1

    yumi.stop()


if __name__ == '__main__':
    main()
