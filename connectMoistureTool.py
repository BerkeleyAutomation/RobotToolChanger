import math
from time import sleep

import tf
from autolab_core import RigidTransform
from yumipy import YuMiRobot
import sys

yumi = YuMiRobot()

def move_YUMI(X, Y, H, ROT0, ROT1, ROT2, V):
    pos = RigidTransform()
    pos.from_frame = 'robot'

    pos.translation = X, Y, H
    quat = tf.transformations.quaternion_from_euler(math.radians(ROT0), math.radians(ROT1), math.radians(ROT2))
    pos.quaternion[0:3] = quat[0:3]
    pos.rotation = RigidTransform.rotation_from_quaternion(quat)
    yumi.set_v(V)
    yumi.right.goto_pose(pos)
    #sleep(.1)


def connect_tool():
    v_very_slow = 50
    v_slow = 100
    v = 200

    h0 = 0.1453+0.131
    h1 = 0.093+0.131

    x0 = 0.394 + 0.052  # y = -0.4303
    x1 = 0.4967 + 0.052  # y = -0.4324
    x2 = 0.5525 + 0.052  # y = -0.4332
    x3 = x2
    x4 = 0.45 + 0.052  # 0.4949  # y = -0.4353
    x5 = 0.394 + 0.052

    y = -0.436+0.035+0.08+0.003

    rot0_0 = 180
    rot0_1 = 155

    rot1_0 = 0
    rot1_1 = -2

    rot2 = 180

    move_YUMI(x0, y, h0, rot0_0, rot1_0, rot2, v) #start point
    move_YUMI(x1, y, h0, rot0_0, rot1_0, rot2, v_slow) #point 1
    move_YUMI(x2, y, h0, rot0_1, rot1_0, rot2, v_very_slow)
    move_YUMI(x3, y, h1, rot0_1, rot1_0, rot2, v_slow)

    x_tmp = x3
    rot_tmp = -2.5
    for i in range(0,22,1):
        x_tmp = x_tmp - 0.0017
        rot_tmp = -rot_tmp
        move_YUMI(x_tmp, y, h1, rot0_1+rot_tmp, rot1_0, rot2, 1000)

    move_YUMI(x5, y, h1, rot0_1, rot1_0, rot2, v)


def disconnect_tool():
    v_very_slow = 50
    v_slow = 100
    v = 200

    # Disconnect tool parameters
    h0 = 0.1453 + 0.131
    h1 = 0.093 + 0.131

    x0 = 0.394 + 0.052  # y = -0.4303
    x1 = 0.4967 + 0.052 # y = -0.4324
    x2 = 0.5533 + 0.052  # y = -0.4332
    x3 = x2
    x4 = 0.495 + 0.052  # y = -0.4353
    x5 = 0.49 + 0.052
    x6 = 0.395 + 0.052

    y = -0.436+0.035+0.08+0.003

    rot0_0 = 180
    rot0_1 = 155

    rot1_0 = 0
    rot1_1 = 2

    rot2 = 180

    move_YUMI(x6, y, h1, rot0_1, rot1_1, rot2, v)
    move_YUMI(x5, y, h1, rot0_1, rot1_1, rot2, v_very_slow)
    move_YUMI(x5 + 0.005, y, h1, rot0_1, rot1_1, rot2, v_very_slow)
    move_YUMI(x5 + 0.01, y, h1, rot0_1, rot1_1, rot2, v_very_slow)
    move_YUMI(x5 + 0.015, y, h1, rot0_1, rot1_1, rot2, v_very_slow)
    move_YUMI(x3, y, h1, rot0_1, rot1_0, rot2, v_very_slow)
    move_YUMI(x2, y, h0, rot0_1, rot1_0, rot2, v_slow)
    move_YUMI(x1, y, h0, rot0_1, rot1_0, rot2, v_slow)
    move_YUMI(x0, y, h0, rot0_1, rot1_0, rot2, v)


def main():
    if len(sys.argv)>1:
        loop = int(sys.argv[1])
    else:
        loop = 1
    itr = 0
    for i in range(0,loop,1):
        print('iteration: ', itr)
        connect_tool()
        disconnect_tool()
        itr = itr + 1

    yumi.stop()


if __name__ == '__main__':
    main()
