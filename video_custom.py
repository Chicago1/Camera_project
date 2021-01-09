#TODO:
#assume the script runs when the computer is turned on
#1. Add a loop that waits for the hard disk to be mounted when the Pi is turned on
#2. Install Shutil on Pi - use this package to monitor disk space and not overfill the filesystem on the hard drive
#3. Compress the day's files and upload them to Google Drive compressed, while storing last uncompressed files on hard drive


import numpy as np
import cv2
import time
from datetime import datetime





#data log time (in seconds)
record_sec = 5

#loops to infinity
while(True):



    # launch video capture software
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    # sets the right codec
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')

    start = time.time()
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    out = cv2.VideoWriter("/home/pi/mnt/gdrive"+dt_string+".mp4", fourcc, 20.0, (640, 480))



    while time.time() - start < record_sec: #
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('frame', frame)
        c = cv2.waitKey(1)
        if c & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    time.sleep(1)












