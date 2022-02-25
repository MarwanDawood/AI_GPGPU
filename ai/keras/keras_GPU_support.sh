#!/bin/sh
# Instal CUDA Toolkit 8.0 for x64 Ubuntu 16.04 

#########################################
# This is part is taken from the repo
#  https://gist.github.com/ksopyla/813a62d6afc4307755e5832a3b62f432
#https://hemenkapadia.github.io/blog/2016/11/11/Ubuntu-with-Nvidia-CUDA-Bumblebee.html

# update packages
sudo apt-get update
sudo apt-get upgrade

sudo apt-get remove --purge nvidia*

#Add the ppa repo for NVIDIA graphics driver
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update

#Install the recommended driver (currently nvidia-378)
sudo ubuntu-drivers autoinstall
sudo reboot

#check if drivers were installed
nvidia-smi
#########################################


sudo apt-get install linux-headers-$(uname -r)
sudo apt-get install mesa-utils

#wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
#sudo dpkg -i cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
# Or run
sudo dpkg -i keras/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
sudo apt-get update
sudo apt-get install cuda-8-0
sudo apt-get autoremove

# Dwonload ccuDNN v5.1 Library for Linux form https://developer.nvidia.com/rdp/cudnn-download
tar -xzf cudnn-8.0-linux-x64-v5.1.tgz 
# copy libs to /usr/local/cuda folder
sudo cp -P cuda/include/cudnn.h /usr/local/cuda/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*

export LD_LIBRARY_PATH=/usr/local/cuda-8.0/targets/x86_64-linux/lib/stubs/:${LD_LIBRARY_PATH}

#know your graphic card version, mine is nvidia quadro 1000M
lspci | grep VGA

#the NVIDIA CUDA Profile Tools Interface
sudo apt-get install libcupti-dev
sudo apt-get install python3-numpy python3-dev python3-pip python3-wheel
sudo reboot

# Ubuntu/Linux 64-bit, GPU enabled, Python 3.5
# Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.1-cp35-cp35m-linux_x86_64.whl
pip3 install --upgrade $TF_BINARY_URL

sudo pip3 install --upgrade tensorflow-gpu # for Python 3.n and GPU

printf "\nintializing tensorflow for the first time\n"
python3 -c "import tensorflow"

printf "\ninstalling Keras now\n"
pip3 install numpy scipy scikit-learn pillow h5py keras

printf "\nintializing keras for the first time\n"
python3  -c "import keras"
