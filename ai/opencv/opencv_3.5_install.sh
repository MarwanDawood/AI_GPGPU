#!/bin/sh

apt-get update
apt-get upgrade

sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

#installing Python bindings
sudo apt-get install python3-dev python3-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff5-dev libdc1394-22-dev

read -p "Download OpenCV from GitHub (y/n)?" choice
if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
git clone https://github.com/opencv/opencv.git
git clone git@github.com:opencv/opencv_contrib.git
fi

cd opencv
mkdir build_2.7
cd build_2.7

#generating native build files (Makefile) for Linux environment with python support and built examples
cmake -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr/local \
      -DBUILD_EXAMPLES=ON \
      -DPYTHON3_EXECUTABLE=/usr/bin/python3.5 \
      -DPYTHON_INCLUDE_DIR=/usr/include/python3.5 \
      -DPYTHON_INCLUDE_DIR2=/usr/include/x86_64-linux-gnu/python3.5m \
      -DPYTHON_LIBRARY=PYTHON_LIBRARY=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu/libpython3.5.so \
      -DPYTHON3_NUMPY_INCLUDE_DIR=/usr/lib/python3/dist-packages/numpy/core/include/ .. \
      -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules/ \
      -DWITH_CUDA=OFF #set to ON if you want CUDA

#building directory
make -j7 # runs 7 jobs in parallel

#installing libraries
sudo make install

sudo apt-get install python-opencv libopencv-dev
