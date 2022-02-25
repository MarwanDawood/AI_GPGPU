import numpy as np
import cv2

img = cv2.imread('images/opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#The parameters here are the image, max corners to detect, quality, and minimum distance between corners.
corners = cv2.goodFeaturesToTrack(gray, 70, 0.1, 10)
corners = np.int0(corners)
print "number of corners", len(corners)

for corner in corners:
    x, y = corner.ravel()
    #thickness = -1 means solid circle
    cv2.circle(img, (x, y), 5, 255, thickness=2)

cv2.imshow('Corner', img)

while True:
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        quit()
