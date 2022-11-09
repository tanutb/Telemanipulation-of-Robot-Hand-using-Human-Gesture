import Module.URclass as UR
import math
from Module.SocketSever import Socket

###### Setup ###########
Server = Socket()                   ## Argument  IP="...." for setup ip
UR_Rb = UR.URRobot()
UR_Rb.sethome()

#### Parameter Setting ####
x2,y2 = 0,0
x2_1,y2_1 = 0,0


def Command_Selection(data):
    Command,lm8_2,lm8_1,lm4_2,lm4_1 = data
    if Command=="Start":
            x = -(((lm8_2/6400)*3)+0.2)
            y = -(((lm8_1/4800)*4)-0.2)
            UR_Rb.moveUR(x,y)
            # print("UR_Rb.moveUR(x,y)")

    elif Command=="Gripper":
        x1,y1 = lm4_1 , lm4_2
        x2,y2 = lm8_1 , lm8_2
        length = math.dist([x1,y1],[x2,y2])
        # print("UR_Rb.GripperControl(length)")
        UR_Rb.GripperControl(length)
    elif Command=="Stop":
        pass
    elif Command=="Home":
        # print("UR_Rb.sethome()")       
        UR_Rb.sethome()
    else:
        pass

###### Run Server ###########
if __name__ == "__main__":
    Server.echo_server(function=Command_Selection)