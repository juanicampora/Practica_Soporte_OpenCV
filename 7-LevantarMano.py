import cv2
import numpy as np

body_parts = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
    "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
        "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
            "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

pose_pairs = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
              ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
              ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
              ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
              ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

image_frame = cv2.imread("images.jpg")

height, width, channel = image_frame.shape
image_width = width
image_height = height

net = cv2.dnn.readNetFromTensorflow("graph_opt.pb")

net.setInput(cv2.dnn.blobFromImage(image_frame, 1.0, (image_width, image_height), (127.5, 127.5, 127.5), swapRB=True, crop=False))
image_output = net.forward()
image_output = image_output[:, :19, :, :]
joints = []
threshold_value = 0.05
frame_height = image_output.shape[2]
frame_width = image_output.shape[3]


for i in range(len(body_parts)):
    # generating confidence map of corresponding body's part.
    probMap = image_output[0, i, :, :]
    
    #  Global maxima of the probMap.
    minimum_value, maximum_value, min_loc, max_loc = cv2.minMaxLoc(probMap)
    
    # Scaling the point
    pt_one = (image_width * max_loc[0]) / frame_width
    pt_two = (image_height * max_loc[1]) / frame_height

    if maximum_value > threshold_value :
        joints.append((int(pt_one), int(pt_two)))

    else :
        joints.append(None)

for pair in pose_pairs:
    first_body_part = pair[0]
    second_body_part = pair[1]
  
    
    part_one = body_parts[first_body_part]
    part_two = body_parts[second_body_part ]
        
    if joints[part_one] and joints[part_two]:
        
        cv2.ellipse(image_frame, joints[part_one], (4, 4), 0, 0, 360, (0, 255, 0), 2)
        cv2.ellipse(image_frame, joints[part_two], (4, 4), 0, 0, 360,(0, 255, 0), 2)
        cv2.line(image_frame, joints[part_one], joints[part_two], (255, 0, 0), 2)

cv2.imshow('OUTPUT IMAGE', image_frame)
cv2.waitKey(0)