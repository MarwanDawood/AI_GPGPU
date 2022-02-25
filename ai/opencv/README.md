[OpenCV Tutorial](https://pythonprogramming.net/loading-images-python-opencv-tutorial/)

# Running phone camera through WiFi network on laptop as a webcam using Python 2.7 only!
1. `Add the file AndroidCamFeed.py` to the working directory
2. Modify the code in file `Camera.py` to include your code after line 22 (the condition check)
3. Download the android application [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en) and start it as a server
4. Get the URL address and the port number and make a command like this
```
python Camera.py 192.168.1.2:8080
```
- - - 
# trining Haar vector to identify watch5050.jpg
```
mkdir data info
opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1100
opencv_createsamples -info info/info.lst -num 1100 -w 20 -h 20 -vec positives.vec
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1000 -numNeg 500 -numStages 10 -w 20 -h 20
```
If you really do want to run the command overnight, but don't want to leave the terminal open, you can make use of nohup:
```
nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20 &
```
If you want to cut down some stages or add stages to the final one you computed, just retype this command with the final total number of stages you need, here we want 11 stages, so we will compute only 1 extra stage
```
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 11 -w 20 -h 20
```
