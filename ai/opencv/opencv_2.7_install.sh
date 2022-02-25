#!/bin/bash

apt-get update
apt-get upgrade

sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

#installing Python bindings
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff5-dev libdc1394-22-dev


read -p "Download OpenCV from GitHub (y/n)?" choice
if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
git clone git@github.com:opencv/opencv.git
git clone git@github.com:opencv/opencv_contrib.git
fi

cd /home/marwan/Desktop/opencv
mkdir build_2.7
cd build_2.7

#generating native build files (Makefile) for Linux environment with python support and built examples
cmake -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr/local \
      -DBUILD_EXAMPLES=ON \
      -DBUILD_OPENCV_PYTHON=ON \
      -DPYTHON2_EXECUTABLE=/usr/bin/python2.7 \
      -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
      -DPYTHON_INCLUDE_DIR2=/usr/include/x86_64-linux-gnu/python2.7 \
      -DPYTHON_LIBRARY=PYTHON_LIBRARY=/usr/lib/python2.7/config-x86_64-linux-gnu/libpython2.7.so \
      -DPYTHON2_NUMPY_INCLUDE_DIR=/usr/lib/python2.7/dist-packages/numpy/core/include/ .. \
      -DOPENCV_EXTRA_MODULES_PATH=~/Desktop/opencv_contrib/modules/ \
      -DWITH_CUDA=OFF #set to ON if you want CUDA

#building directory
make -j7 # runs 7 jobs in parallel

#installing libraries
sudo make install

sudo apt-get install python-opencv libopencv-dev

