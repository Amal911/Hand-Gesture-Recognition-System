
import cv2
import time
import numpy as np
import HandTrackinModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
import pyautogui

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7, maxHands=2)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

minBrightness = 0
maxBrightness = 100

btooth = 0
wifi= 0

while True:
    success , img = cap.read()
    img = cv2.flip(img, 1)



    cTime = time.time()
    fps =  1/(cTime-pTime)
    pTime = cTime




    img = detector.findHands(img)
    lmList, handedness = detector.findPosition(img, draw= False)
    # fingers = detector.fingersUp(lmList)

    if handedness == "Left":
        
        fingers = detector.fingersUp(lmList)
        # Volume
        if fingers[1] and not fingers[0] and not fingers[2] and not fingers[3] and not fingers[4] :

            while True:
                success , img = cap.read()
                img = cv2.flip(img, 1)
                cTime = time.time()
                fps =  1/(cTime-pTime)
                pTime = cTime
                img = detector.findHands(img)
                lmList, handedness = detector.findPosition(img, draw= False)

                if len(lmList)!=0:
                    x1, y1 = lmList[8][1], lmList[8][2]
                    
                    fingers = detector.fingersUp(lmList)
                    vol = 100 - np.interp(y1, [100, 380], [0, 100])
                    vol= int(vol)
                    # print(vol)
                    vol = np.interp(vol, [0, 100], [minVol, maxVol])

                    # if not fingers[4] and not fingers[3] and not fingers[2]:
                    volume.SetMasterVolumeLevel(vol, None)

                    break
                cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0, 3))
                cv2.imshow("Img", img)
                cv2.waitKey(1)

        # Bluetooth
        elif fingers[1] and fingers[2] and not fingers[3] and not fingers[4] :

            while True:
                success , img = cap.read()
                img = cv2.flip(img, 1)
                cTime = time.time()
                fps =  1/(cTime-pTime)
                pTime = cTime
                img = detector.findHands(img)
                lmList, handedness = detector.findPosition(img, draw= False)

                if len(lmList)!=0:
                    
                    fingers = detector.fingersUp(lmList)
                    if not fingers[1] and not fingers[2] and not fingers[3] and not fingers[3]:

                        if not btooth:
                            btooth = 1
                            print("Bluetooth on")
                            break
                        elif btooth:
                            btooth = 0
                            print("Bluetooth off")
                            break
                    break
                cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0, 3))
                cv2.imshow("Img", img)
                cv2.waitKey(1)
        # Zoom Out
        elif  fingers[1] and  fingers[0] and not fingers[2] and not fingers[3] and not fingers[4] :
            while True:
                success , img = cap.read()
                img = cv2.flip(img, 1)
                cTime = time.time()
                fps =  1/(cTime-pTime)
                pTime = cTime
                img = detector.findHands(img)
                lmList, handedness = detector.findPosition(img, draw= False)

                if len(lmList)!=0:
                    
                    fingers = detector.fingersUp(lmList)
                    if not fingers[1] and  fingers[0] and not fingers[2] and not fingers[3] and not fingers[4]:
                        print("Zoom Out")
                        pyautogui.keyDown("ctrl")
                        pyautogui.press("-")
                        pyautogui.keyUp("ctrl")
                    break
                # cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0, 3))
                # cv2.imshow("Img", img)
                # cv2.waitKey(1)


       
    elif handedness == "Right":
        # Brightness
        fingers = detector.fingersUp(lmList)
        if  fingers[1] and  fingers[0] and not fingers[2] and not fingers[3] and not fingers[4] :

            while True:
                success , img = cap.read()
                img = cv2.flip(img, 1)
                cTime = time.time()
                fps =  1/(cTime-pTime)
                pTime = cTime
                img = detector.findHands(img)
                lmList, handedness = detector.findPosition(img, draw= False)

                if len(lmList)!=0:
                    x1, y1 = lmList[8][1], lmList[8][2]
                    
                    fingers = detector.fingersUp(lmList)
                    
                    brightness = 100 - np.interp(y1, [100, 380], [0, 100])
                    brightness= int(brightness)
                    # print(vol)
                   
                    sbc.set_brightness(int(brightness))
                    
                    break
        # WIFI
        elif fingers[1] and fingers[2] and not fingers[3] and not fingers[4]:

            while True:
                success , img = cap.read()
                img = cv2.flip(img, 1)
                cTime = time.time()
                fps =  1/(cTime-pTime)
                pTime = cTime
                img = detector.findHands(img)
                lmList, handedness = detector.findPosition(img, draw= False)

                if len(lmList)!=0:
                    
                    fingers = detector.fingersUp(lmList)
                    if not fingers[1] and not fingers[2] and not fingers[3] and not fingers[3]:
                        if not wifi:
                            wifi = 1
                            print("wifi on")
                            break
                        elif wifi:
                            wifi = 0
                            print("wifi off")
                            break
                    break

                cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0, 3))
                cv2.imshow("Img", img)
                cv2.waitKey(1)
        # Zoom IN
        elif  not fingers[1] and  fingers[0] and not fingers[2] and not fingers[3] and not fingers[4] :
            
            while True:
                
                success , img = cap.read()
                img = cv2.flip(img, 1)
                cTime = time.time()
                fps =  1/(cTime-pTime)
                pTime = cTime
                img = detector.findHands(img)
                lmList, handedness = detector.findPosition(img, draw= False)

                if len(lmList)!=0:
                    
                    fingers = detector.fingersUp(lmList)
                    if  fingers[1] and not fingers[0]:
                        print("Zoom In")
                        pyautogui.keyDown("ctrl")
                        pyautogui.press("+")
                        pyautogui.keyUp("ctrl")
                    break
                
                # cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0, 3))
                # cv2.imshow("Img", img)
                # cv2.waitKey(1)



    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0, 3))

    cv2.imshow("Img", img)
    cv2.waitKey(1)