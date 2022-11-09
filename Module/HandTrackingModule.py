

import cv2
import mediapipe as mp



class handTracker():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.imlist = []
        self.socket = ''
        
    def handsFinder(self,image,draw=True):
        imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image
    
    def positionFinder(self,image, handNo=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            Hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(Hand.landmark):
                h,w,c = image.shape
                cx,cy,cz = int(lm.x*w), int(lm.y*h),lm.z
                lmlist.append([id,cx,cy,cz])
                if id == 8:
                    if draw:
                        cv2.circle(image,(cx,cy), 15 , (255,0,0), cv2.FILLED)


        return lmlist

    def HandStatus(self,lmlist):
        Status = [False,False,False,False,False]
        Thumb_stat = lmlist[4][1] - lmlist[10][1] 
        Index_stat = lmlist[8][2] - lmlist[5][2]
        Middle_stat = lmlist[12][2] -lmlist[9][2]
        Ring_stat = lmlist[16][2] - lmlist[13][2]
        Pinky_stat = lmlist[20][2] - lmlist[17][2]
        Finger_distance = [Thumb_stat,Index_stat,Middle_stat,Ring_stat,Pinky_stat]
        for i in range(len(Status)):
            if Finger_distance[i]<0:
                Status[i]=True
            else: Status[i]=False

        if Thumb_stat <=25 and Thumb_stat >=-25:
            Status[0] = False
        else:
            Status[0] = True
        return Status

    def CommandforUR(self,Status):
        Start = [False,True,False,False,False]
        Stop = [True,True,True,True,True]
        Home = [False,False,False,False,False]
        Gripper = [True,True,False,False,True]
        if Status == Start or Status == [True,True,False,False,False]:
            return "Start"
        elif Status == Home:
            return "Home"
        elif Status == Stop:
            return "Stop"
        elif Status == Gripper:
            return "Gripper"
        else:
            return None
    
    def main(self):
        cap = cv2.VideoCapture(0)
        tracker = handTracker()
        while True:
            success,image = cap.read()
            image = tracker.handsFinder(image)
            self.lmList = tracker.positionFinder(image)
            cv2.imshow("Video",image)
            cv2.waitKey(1)


