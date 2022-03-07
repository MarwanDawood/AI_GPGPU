import cv2
import numpy as np
from cv2 import CV_LOAD_IMAGE_GRAYSCALE, CV_LOAD_IMAGE_UNCHANGED


img_rgb = cv2.imread('images/opencv-template-matching-python-tutorial.jpg', flags=CV_LOAD_IMAGE_UNCHANGED)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


template = cv2.imread('images/opencv-template-for-matching.jpg',flags=CV_LOAD_IMAGE_GRAYSCALE)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.8
#creating new array of elements coordinates that exceeds only the threshold coefficient
loc = np.where( res >= threshold)

#unzipping the 2 arrays to get a tuple of x,y coordinates
for pt in zip(*loc[::-1]):
    print pt
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)

while True:
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        quit()
