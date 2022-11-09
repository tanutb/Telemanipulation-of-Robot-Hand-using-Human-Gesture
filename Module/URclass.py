import rtde_control
import rtde_receive
from robotiq_gripper_control import RobotiqGripper
import numpy as np
import rtde_io

class URRobot():
    def __init__(self):
        self.ip = "192.168.20.35"
        self.rtde_c     = rtde_control.RTDEControlInterface(self.ip)
        self.rtde_r     = rtde_receive.RTDEReceiveInterface(self.ip)    
        self.rtde_io_   = rtde_io.RTDEIOInterface(self.ip)
        self.state_stop = self.rtde_c.getAsyncOperationProgress()
    
    def sethome(self):
        qbase = np.pi*0
        qshouder = -np.pi/3
        qelbow = np.pi/3
        qwrist1 = np.pi*0
        qwrist2  = np.pi/2
        qwrist3 = np.pi/3
        self.rtde_c.moveJ([qbase, qshouder, qelbow, qwrist1, qwrist2, qwrist3], 0.5, 0.3)

    def moveUR(self,x,y):
        if x > -0.2 :
            x = -0.2
        elif  x <-0.5:
            x = -0.5
        if y > 0.2:
            y = 0.2
        elif  y <-0.2:
            y = -0.2
        if self.state_stop < 0:
            self.rtde_c.moveJ_IK([x, y, 0.2771877876472226, 0.4189044692262709, -1.52750664380437, -0.4114795078640724], 0.5, 0.3)
        actual_TCPpose = self.rtde_r.getActualTCPPose()

    def GripperControl(self,length):
        if length <= 50:
            self.rtde_io_.setStandardDigitalOut(0, True)
            self.rtde_io_.setStandardDigitalOut(1, False)
        else:
            self.rtde_io_.setStandardDigitalOut(0, False)
            self.rtde_io_.setStandardDigitalOut(1, True)
