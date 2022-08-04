import numpy as np
import cv2
import cv2.aruco as aruco

cap = cv2.VideoCapture(0)
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

while (True):
    
    ret, frame = cap.read() # Capturamos una imagen a la vez
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    #print(ids)

    frame = aruco.drawDetectedMarkers(frame, corners)

    
    cv2.imshow('frame', frame) # Mostramos en la imagen los ArUcos encontrados
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release() # Liberamos la cámara al final de la utilización 
cv2.destroyAllWindows()