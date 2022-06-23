import cv2
import numpy as np

img_path = 'paris.jpg'

img_raw = cv2.imread(img_path)

roi = cv2.selectROI (img_raw)

print(roi)

roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]

cv2.imshow('ROI', roi_cropped)

cv2.imwrite('parisRecortada.jpeg', roi_cropped)

cv2.waitkey(0)