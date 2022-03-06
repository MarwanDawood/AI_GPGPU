import cv2
import numpy as np
import sys
from AndroidCamFeed import AndroidCamFeed

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#this is the cascade we just made. Call what you want
watch_cascade = cv2.CascadeClassifier('data/watch_cascade_10_stages.xml.xml')

def main():
    if not sys.argv[1] or len(sys.argv) > 2:
        print "Usage: \n\tpython Example.py <host>:<port>"
        return

    # Set host
    host = sys.argv[1]

    # Create new AndroidCamFeed instance
    cap = AndroidCamFeed(host)

    # While camera is open
    while cap.isOpened():
        ## Read frame
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frm, (910, 512))    # Resize image
## ADD YOUR CODE HERE!
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            lower_red = np.array([30,150,50])
            upper_red = np.array([255,255,180])

            mask = cv2.inRange(hsv, lower_red, upper_red)
            res = cv2.bitwise_and(frame,frame, mask= mask)

            laplacian = cv2.Laplacian(frame,cv2.CV_64F)
            # x=1, y=0, convolution kernel is 5x5
            sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
            # x=0, y=1, convolution kernel is 5x5
            sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

            edges = cv2.Canny(frame,100,200)
            cv2.imshow('Edges',edges)
## END OF YOUR CODE!

        # delay in 5 milliseconds
        k = cv2.waitKey(5) & 0xFF
        # 27 is the escape character
        if k == 27:
            break

    # Must Release ACF instance
    cv2.destroyAllWindows()
    cap.release()
    return


if __name__ == '__main__':
    main()
