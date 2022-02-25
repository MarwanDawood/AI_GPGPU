import cv2
import numpy as np

img = cv2.imread('images/bookpage.jpg')
retval, threshold1 = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold1',threshold1)


grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold2 = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('grayscaled',grayscaled)
cv2.imshow('threshold2',threshold2)

threshold3 = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Adaptive threshold',threshold3)


cv2.waitKey(0)
cv2.destroyAllWindows()
