import pygame
from time import sleep
from yumipy import YuMiRobot
import datetime
import pickle
from autolab_core import RigidTransform
import tf
import math
import threading

yumi = YuMiRobot()
pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

stop_btn = 0

def disconnect_tool(pos_num):
    global stop_btn
    while stop_btn==0:
        pygame.event.pump()
        btn_y = pygame.joystick.Joystick(0).get_button(4)
        stop_btn = pygame.joystick.Joystick(0).get_button(0)
        if btn_y == 1:
            break
    X = 0
    Y = 0
    H = 0
    V = 0
    pos = RigidTransform()
    pos.from_frame = 'robot'

    h0 = 0.1453
    h1 = 0.094

    x0 = 0.394  # y = -0.4303
    x1 = 0.4967  # y = -0.4324
    x2 = 0.5533  # y = -0.4332
    x3 = x2
    x4 = 0.4949  # y = -0.4353
    x5 = 0.489
    x6 = 0.394

    y = -0.4365

    rot0_0 = 180
    rot0_1 = 155

    rot1_0 = 0
    rot1_1 = 2

    v_very_slow = 50
    v_slow = 100
    v = 200

    if pos_num == 0:
        X, Y, H, ROT0, ROT1, V = x6, y, h1, rot0_1, rot1_0, v
    elif pos_num == 1:#NEW point
        X, Y, H, ROT0, ROT1, V = x5, y, 0.0964, rot0_1, rot1_0, v
    elif pos_num == 2:
        X, Y, H, ROT0, ROT1, V = x4, y, h1, rot0_1, rot1_0, v_very_slow
    elif pos_num == 3:
        X, Y, H, ROT0, ROT1, V = x3, y, h1, rot0_1, rot1_0, v_very_slow
    elif pos_num == 4:
        X, Y, H, ROT0, ROT1, V = x2, y, h0, rot0_1, rot1_0, v_slow
    elif pos_num == 5:
        X, Y, H, ROT0, ROT1, V = x1, y, h0, rot0_1, rot1_0, v_slow
    elif pos_num == 6:
        X, Y, H, ROT0, ROT1, V = x0, y, h0, rot0_1, rot1_0, v

    pos.translation = X, Y, H
    quat = tf.transformations.quaternion_from_euler(math.radians(ROT), math.radians(0), math.radians(180))
    pos.quaternion[0:3] = quat[0:3]
    pos.rotation = RigidTransform.rotation_from_quaternion(quat)
    yumi.set_v(V)
    yumi.right.goto_pose(pos)
    sleep(.3)


def connect_tool(pos_num):
    global stop_btn
    while stop_btn==0:
        pygame.event.pump()
        btn_y = pygame.joystick.Joystick(0).get_button(4)
        stop_btn = pygame.joystick.Joystick(0).get_button(0)
        if btn_y == 1:
            break

    X = 0
    Y = 0
    H = 0
    V = 0
    pos = RigidTransform()
    pos.from_frame = 'robot'

    h0 = 0.1453
    h1 = 0.094

    x0 = 0.394  # y = -0.4303
    x1 = 0.4967  # y = -0.4324
    x2 = 0.5533  # y = -0.4332
    x3 = x2
    x4 = 0.45 #0.4949  # y = -0.4353
    x5 = 0.394

    y = -0.436

    rot0_0 = 180
    rot0_1 = 155

    rot1_0 = 0
    rot1_1 = -2

    v_very_slow = 50
    v_slow = 100
    v = 200

    if pos_num == 0:
        X, Y, H, ROT0, ROT1, V = x0, y, h0, rot0_0, rot1_0, v
    elif pos_num == 1:
        X, Y, H, ROT0, ROT1, V = x1, y, h0, rot0_0, rot1_0, v_slow
    elif pos_num == 2:
        X, Y, H, ROT0, ROT1, V = x2, y, h0, rot0_1, rot1_0, v_very_slow
    elif pos_num == 3:
        X, Y, H, ROT0, ROT1, V = x3, y, h1, rot0_1, rot1_0, v_slow
    elif pos_num == 4:
	X, Y, H, ROT0, ROT1, V = x3 - 0.015, y, h1, rot0_1, rot1_0, v_slow
    elif pos_num == 5:
        X, Y, H, ROT0, ROT1, V = x4, y, h1, rot0_1, rot1_1, 300
    elif pos_num == 6:
        X, Y, H, ROT0, ROT1, V = x5, y, h1, rot0_1, rot1_0, v

    pos.translation = X, Y, H
    quat = tf.transformations.quaternion_from_euler(math.radians(ROT0), math.radians(ROT1), math.radians(180))
    pos.quaternion[0:3] = quat[0:3]
    pos.rotation = RigidTransform.rotation_from_quaternion(quat)
    yumi.set_v(V)
    yumi.right.goto_pose(pos)
    sleep(.3)

def main():
    global stop_btn
    try:
        while stop_btn==0:
            for i in range(0,6,1):
                connect_tool(i)
            if stop_btn==1:
                continue
            for i in range(0, 5, 1):
                disconnect_tool(i)
    except:
        pass

    yumi.stop()

if __name__ == '__main__':
    main()
