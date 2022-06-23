import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame=cap.read()

    cv2.imshow('Camara Notebook',frame)
    if cv2.waitKey(1) & 0xff == 27: #27 es la tecla ESCAPE
      break

cap.release()
cv2.destroyAllWindows()