import cv2
import mediapipe as mp
from copy import deepcopy
import time
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
itera=True
temporizando=False
numeronombre=0
while True:
    success, image = cap.read()
    image=cv2.resize(image, (800, 700))
    image=cv2.flip(image,1)
    original = deepcopy(image)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    itera=not(itera)
 # checking whether a hand is detected
    afuera=True
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if ((600<cx<800) and (0<cy<200)):
                    if itera:
                        cv2.rectangle(image,(600,0),(800,200),(0,255,0),-1)
                    afuera=False
            #mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS,mpDraw.DrawingSpec(color=(57,110,151), thickness=2, circle_radius=2),
            mpDraw.DrawingSpec(color=(82,155,212), thickness=2, circle_radius=2))
        if afuera:
            cv2.rectangle(image,(600,0),(800,200),(0,0,255),2)
    cv2.rectangle(original, (600, 0), (800, 200), (90, 90, 81), 2)
    cv2.imshow("Analisis", image)
    cv2.imshow("Original", original)
    tecla= cv2.waitKey(1)
    if tecla==27:
        break
    elif tecla==32:
        iniciotemp=time.time()
        temporizando=True
    if temporizando and (time.time()-iniciotemp)>=5:
        numeronombre+=1
        numeronombreconcero=str(numeronombre).rjust(5, '0')
        nombre=f"imagen {numeronombreconcero}.png"
        cv2.imwrite(str(nombre), original)
        cv2.imshow('infraccion ', original)
        temporizando=False
