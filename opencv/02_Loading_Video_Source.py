import numpy as np
import cv2

#camera id
cap = cv2.VideoCapture(0)
#video codec object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#video write text object
out = cv2.VideoWriter('images/output.avi',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
