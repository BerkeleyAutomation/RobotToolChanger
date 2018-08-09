import pygame
from time import sleep
from yumipy import YuMiRobot
import datetime
import pickle

def main():

    pygame.display.init()
    pygame.joystick.init()
    pygame.joystick.Joystick(0).init()

    # starting the robot interface
    print('RTK')
    y = YuMiRobot()
    data = []
    pointNum=0

    while True:
        pygame.event.pump()
        btn_y = pygame.joystick.Joystick(0).get_button(4)
        btn_a = pygame.joystick.Joystick(0).get_button(0)
        if btn_y==1:
            data.append(y.right.get_pose())
            pointNum=pointNum+1
            print 'point recorded'
            sleep(.3)
        if btn_a==1:
            break
    # now = datetime.datetime.now()
    # timeStr = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+":"+str(now.microsecond)

    pickle.dump(data, open("/home/ron/Desktop/YUMI_POS.p", "wb"))

if __name__ == '__main__':
    main()
    
# from yumipy import YuMiRobot
# starting the robot interface
# getting the current pose of the right end effector
#pose = y.right.get_pose()
# print(pose)
# # move right arm forward by 5cm using goto_pose
# pose.translation[0] += 0.05
# y.right.goto_pose(pose)
# # move right arm back by 5cm using move delta
# y.right.goto_pose_delta((-0.05,0,0))