#TODO:
#assume the script runs when the computer is turned on
#1. Add a loop that waits for the hard disk to be mounted when the Pi is turned on
#2. Install Shutil on Pi - use this package to monitor disk space and not overfill the filesystem on the hard drive
#3. Add a while True loop that


import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('/home/pi/Desktop/cctv/output.mp4', fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)
    c = cv2.waitKey(1)
    if c & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindowqs()