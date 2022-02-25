import numpy as np
import cv2
import matplotlib.pyplot as plt
from cv2 import CV_LOAD_IMAGE_GRAYSCALE


img1 = cv2.imread('images/opencv-feature-matching-template.jpg',flags = CV_LOAD_IMAGE_GRAYSCALE)
img2 = cv2.imread('images/opencv-feature-matching-image.jpg',flags = CV_LOAD_IMAGE_GRAYSCALE)

#This is the detector we're going to use for the features
#some openCV use cv2.ORB_create() instead
orb = cv2.ORB()

#Here, we find the key points and their descriptors with the orb detector
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)


#This is our BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)


#Here we create matches of the descriptors, then we sort them based on their distances
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

#this is not working on Python 2.7!
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None)

plt.imshow(img3)
plt.show()


