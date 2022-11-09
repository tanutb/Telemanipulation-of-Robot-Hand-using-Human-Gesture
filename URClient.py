import Module.HandTrackingModule as htm
import cv2
from Module.SocketSever import Socket

##### Setup ##########
HandDetector = htm.handTracker(detectionCon=0.7)
Client = Socket(IP="127.0.0.1")
# Client = Socket()
Client.client_connect()
draw = True
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)


if __name__ == "__main__":
    while 1 :
        success ,img = cap.read()
        HandDetector.handsFinder(img,draw=draw)
        lmlist = HandDetector.positionFinder(img,draw=draw)
        if len(lmlist)>=21:
            HandStatus = HandDetector.HandStatus(lmlist)
            Command = HandDetector.CommandforUR(HandStatus)
            
            arr = [Command,lmlist[8][2],lmlist[8][1],lmlist[4][2],lmlist[4][1]]
            Client.client_send_data(arr)               

        cv2.imshow("Img",img)
        cv2.waitKey(1)