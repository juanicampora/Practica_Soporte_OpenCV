import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame=cap.read()
    grisFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('En Gris',grisFrame)
    if cv2.waitKey(1) & 0xff == 27:
      break

cap.release()
cv2.destroyAllWindows()