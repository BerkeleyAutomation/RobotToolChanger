import pickle
from autolab_core import RigidTransform
import numpy as np

# data = pickle.load(open("/home/ron/Desktop/YUMI_POS.p",'rb'))
# pos1 = data[1]
# pos2 = data[2]

h0 = 0.1453
h1 = 0.0974

x0 = 0.394 #y = -0.4303
x1 = 0.4967 #y = -0.4324
x2 = 0.5533 #y = -0.4332
x3 = 0.5533
x4 = 0.4949 #y = -0.4353
x5 = -0.883

y = -0.4324

rot0 = 0

rot1 = 0

pos0 = RigidTransform()

pos0.translation = x0, y, h0

#
# pos.translation = pos1.translation
# pos.quaternion = 0,1.57,0,0.99
# # RT.quaternion
# # pos1.translation = 0,0,0
# print(pos.rotation)
# # pos1.quaternion[0] = 0
#
# # print(pos1.rotation)
# # print(pos1.translation, pos1.to_frame,)
