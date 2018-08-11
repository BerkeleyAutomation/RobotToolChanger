import pygame
from time import sleep
# from yumipy import YuMiRobot
import datetime
import pickle
from yumipy import YuMiConstants as YMC
from yumipy import YuMiSubscriber

def main():

    pygame.display.init()
    pygame.joystick.init()
    pygame.joystick.Joystick(0).init()

    sub = YuMiSubscriber()    
    sub.start()

    # starting the robot interface
    print('RTK')
    data = []
    pointNum=0

    while True:
        pygame.event.pump()
        btn_y = pygame.joystick.Joystick(0).get_button(4)
        btn_a = pygame.joystick.Joystick(0).get_button(0)
        if btn_y==1:
            _, pose_r = sub.right.get_pose()
            data.append(pose_r)
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