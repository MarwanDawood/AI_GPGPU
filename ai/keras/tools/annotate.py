#https://www.learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/

import cv2
import numpy as np
 
#if __name__ == '__main__' :
 
# Read image
im = cv2.imread("bus.jpg")
    
while True: 
    # Select ROI
    r = cv2.selectROI(im)

    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    if r[0] == 0 and r[1] == 0 and r[2] == 0 and r[3] == 0 :
        break

    print ("(" + str(r[1]) + "," + str(r[1]+r[3]) + "),(" + str(r[0]) + "," + str(r[0]+r[2]) + ")")

    # Display cropped image
    #cv2.imshow("Image", imCrop)
        
cv2.destroyAllWindows()
quit() 
