import cv2
import numpy as np

img = cv2.imread('images/cups.jpg',cv2.IMREAD_COLOR)

#reference specific pixels
px = img[55,55]
#actually change a pixel:
img[55,55] = [255,255,255]
px = img[55,55]
#print pixle color value
print(px)

#Next, we can reference an ROI, or Region of Image, like so:
px = img[100:150,100:150]
print(px)
#We can also modify the ROI, like this:
img[100:150,100:150] = [255,255,255]
#We can reference certain characteristics of our image:
print(img.shape)
print(img.size)
print(img.dtype)

#And we can perform operations, like:
watch_face = img[150:400,70:210]
img[0:250,0:140] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
