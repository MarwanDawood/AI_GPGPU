This project was developed based on this [OpenCV Tutorial](https://pythonprogramming.net/loading-images-python-opencv-tutorial/).

# Installation
Run on Linux one of the following shell scripts, Python 2.7 is prefered though as it supports IP webcam.
```
./opencv_2.7_install.sh
./opencv_3.5_install.sh
```
The files can be loaded offline or online via a webcam.
## Running phone camera through WiFi network on laptop as a webcam using Python 2.7 only!
1. `Add the file AndroidCamFeed.py` to the working directory
2. Modify the code in file `Camera.py` to include your code after line 29, the code would be any OpenCV filter used in this project.
3. Download the android application [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en) and start it as a server
4. Get the URL address and the port number and make a command like this
```
python2.7 Camera.py 192.168.178.176:8080
```
### Edge filter
Applying Edge filter to the webcam video stream yeilds the following
[webcam edge filter](images/01_webcam_edges.png)

### Color mask
Applying color mask to pass only the colors in the RGB range from 30,150,50 to 255,255,180 as shown below.
[color mask](images/02_color_ref.png) [color filter](images/02_color_filter.png)

# Trining Haar Cascade vector (depreciated)
_Haar Cascade are depreciated after OpenCV v.3.4 since deep neural networks provide much better results._
OpenCV offers the opportunity to traing Haar vector to identify objects.
The below image shall be the validator dataset.
[validator image](watch5050.jpg)

```
mkdir haar_training
cd haar_training
mkdir data info

opencv_createsamples -img ../watch5050.jpg -bg bg.txt -info haar_training/info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1100
opencv_createsamples -info haar_training/info/info.lst -num 1100 -w 20 -h 20 -vec haar_training/positives.vec
```
To train the Haar vector, the original command is below, although there is some tuning that can be applied in the following commands.
```
opencv_traincascade -data data -vec haar_training/positives.vec -bg haar_training/bg.txt -numPos 1000 -numNeg 500 -numStages 10 -w 20 -h 20
```
## 1. To cut down some stages or add stages to the final one you computed
Just retype this command with the final total number of stages you need, here we want 11 stages, so we will compute only 1 extra stage
```
opencv_traincascade -data haar_training/data -vec positives.vec -bg haar_training/bg.txt -numPos 1800 -numNeg 900 -numStages 11 -w 20 -h 20
```
## 2. To run the command overnight
but don't want to leave the terminal open, you can make use of nohup:
```
nohup opencv_traincascade -data haar_training/data -vec haar_training/positives.vec -bg haar_training/bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20 &
```