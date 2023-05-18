import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode =False,maxHands = 1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True ):
        
        imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks: 
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img
    
    def findPosition(self, img, handNo=0, draw= True):
        lmList = []
        handedness = []
        if self.results.multi_hand_landmarks:
            myHands = self.results.multi_hand_landmarks[handNo]
            handedness = self.results.multi_handedness[0].classification[0].label
            for id, lm in enumerate(myHands.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y *h)
                # print(id, cx, cy)
                lmList.append([id, cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy),5, (255,0,255), cv2.FILLED)
            
        return lmList, handedness



    def fingersUp(self,lmList):
        fingers = []
        tipIds = [4, 8, 12, 16, 20]
        # thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #4 Fingers
        for id in range(1 ,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers




# if results.multi_hand_landmarks:
#     for handLms in results.multi_hand_landmarks:
#         mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)



def main():
    cap = cv2.VideoCapture(0)
    detector= handDetector()
    pTime = 0
    cTime = 0
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList)!=0:
            print(lmList[4])

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0, 3))

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()