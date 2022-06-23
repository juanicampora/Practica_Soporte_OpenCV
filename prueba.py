import cv2

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()
  ret, frame1= cap.read()
  gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

# Escribe texto en el frame 1
  font = cv2.FONT_HERSHEY_SIMPLEX
  cv2.putText(frame,
              'Con la Q salis del video',
              (10, 50),
              font, 1,
              (0, 0, 255),
              2,
              cv2.LINE_4)

  #Esto muestra los videos
  cv2.imshow('Ventana 1', frame)
  cv2.imshow('Ventana 2', gray)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.distroyAllWindows()