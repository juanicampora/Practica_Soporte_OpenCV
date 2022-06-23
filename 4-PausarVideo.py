import numpy as np
import cv2

cap = cv2.VideoCapture(0)
pausado=True
while(True):
    ret, frame=cap.read()
    
    if (cv2.waitKey(1)== 32): #27 es la tecla ESPACIO
      pausado=not(pausado)
     
    if pausado:
      cv2.imshow('Camara Notebook',frame)
      
    if cv2.waitKey(1)== 27: #27 es la tecla ESCAPE
      break 


cap.release()
cv2.destroyAllWindows()