# Deteccion Tortillas 0.0.1

# Import Computer Vision package - cv2
import cv2

# Import Numerical Python package - numpy as np
import numpy as np

capture = cv2.VideoCapture(0)

#esto es una pruebal de background
fgbg = cv2.createBackgroundSubtractorMOG2()



while True:
    ret, cap_cam = capture.read()

    fgmask = fgbg.apply(cap_cam)

    # Height and width of the frames are taken 
    frame_height, frame_width = cap_cam.shape[:2]

    # Define box dimensions at the center of the frame
    x1_top_left = frame_width / 5
    y1_top_left = (frame_height / 2) + (frame_height / 4)
    x2_bottom_right = (frame_width / 3) + 250
    y2_bottom_right = (frame_height / 2) - (frame_height / 4)

    # Rectangular box is drawn around the box dimensions using cv2.rectangle built-in function
    # cv2.rectangle(capturing, (x1,y1), (x2,y2), color, thickness)
    cv2.rectangle(cap_cam, (x1_top_left,y1_top_left), (x2_bottom_right,y2_bottom_right), (0,0,255), 2)


    # Rectangular box region defined above is cropped 
    cropped_box = cap_cam[y2_bottom_right:y1_top_left , x1_top_left:x2_bottom_right]
    

    # Captured frame is flipped horizontally using cv2.flip built-in function
    # Horizontal flipping of images using value '1'
    cap_cam = cv2.flip(cap_cam,1)

    # Display object detected using imshow built-in function
    cv2.imshow('Deteccion Tortillas', cap_cam)
    cv2.imshow('Sin Fondo',fgmask)


    # Check if the user has pressed Esc key
    c = cv2.waitKey(1)
    if c == 27:
        break
