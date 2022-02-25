import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/opencv-python-foreground-extraction-tutorial.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
print mask
print np.shape(mask)
print mask.argmax()

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (139,79,274,158)
pt1 = rect[0:2]
pt2 = rect[2:4]
# draw a rectangle to know your boundaries
#cv2.rectangle(img,pt1,pt2,(255,0,0), thickness=2)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
print mask.argmax()

# if condition is true, return 0 ,else return 1
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
print np.shape(mask2)
print mask2.argmax()

img = img*mask2[:,:,np.newaxis]
print np.shape(img)


plt.imshow(img)
plt.colorbar()
plt.show()
