import cv2
import numpy as np

# Load two images of same size
img1 = cv2.imread('images/3D-Matplotlib.png')
#img2 = cv2.imread('images/mainsvmimage.png')
img2 = cv2.imread('images/mainlogo.png')

#superpositioning images
#add = img1+img2

#adding pixel values, if value exceeds 255, then it is 255 i.e. white
#add = cv2.add(img1,img2)

#parameters are the images, weights, and then finally gamma, which is a measurement of ligh
#weighted = cv2.addWeighted(img1, 0.3, img2, 0.8, 0)

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
print rows ,cols, channels
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

#python logo symbol is black
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI, so you can get the background of logo merged with the bigger image
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image, and superimpose it to the logo
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst


cv2.imshow('mask',mask)
cv2.imshow('dst',dst)
cv2.imshow('img1',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
