import numpy as np
import cv2

cap = cv2.VideoCapture(0)
pausado=True
while(True):
    ret, frame=cap.read()
    
    tecla=cv2.waitKey(1)

    if tecla== 32: #27 es la tecla ESPACIO
      pausado=not(pausado)
    elif tecla== 27:
      break    
    
    if pausado:
      cv2.imshow('Camara Notebook',frame)

cap.release()
cv2.destroyAllWindows()