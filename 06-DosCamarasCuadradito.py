import numpy as np
import cv2
import copy

cap = cv2.VideoCapture(0)
titilar=True
while(True):
    ret, frame=cap.read()
    frame = cv2.resize(frame, (500, 500))
    frame1=copy.deepcopy(frame)
    frame2=copy.deepcopy(frame)

    cv2.rectangle(frame1,(400,0),(500,100),(0,255,0),1)
    if titilar:
        cv2.rectangle(frame2,(400,0),(500,100),(0,255,0),-8)
    titilar=not(titilar)
    cv2.imshow('Camara Notebook',frame1)
    grisFrame = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    cv2.imshow('En Gris',grisFrame)

    if cv2.waitKey(1) & 0xff == 27: #27 es la tecla ESCAPE
      break

cap.release()
cv2.destroyAllWindows()