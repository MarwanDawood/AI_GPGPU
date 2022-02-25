This project ran on PyCharm IDE with keras interpreter extension to support auto complete

# Switching between different environments
```
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh
workon open_cv_3
```
# Creating a new environment
```
export WORKON_HOME=~/Envs
source /home/marwan/.local/bin/virtualenvwrapper.sh 
mkvirtualenv <env>
workon <env>
```
- - -

# Keras Tensorflow installation for Ubuntu 17.04 (Zesty Zapus)

[Install Keras with Tensorflow complete guide](http://www.pyimagesearch.com/2016/11/14/installing-keras-with-tensorflow-backend/)
Tensorflow requires GPUs of compute capability 3.0 or higher for GPU acceleration and this has been true since the very first release of tensorflow.
path of Keras installation is `~/Envs/keras_tf/`

## Running Keras installation scripts for CPU only with virtual environment
modify first `CURRENT_USER` environment variable then run the following
```
source keras_virtualenv.sh
source keras_CPU_only_support.sh
```

>after successful installation, try one of Keras examples like `python ~/Envs/keras_tf/keras/examples/addition_rnn.py`, if an error occurred, then try reinstalling tensorflow again through the command `pip install --upgrade tensorflow`

## Running OpenCV installation scripts
```
source opencv_3.5_install.sh
```

## Installing tensorflow GPU support in addition to CPU
```
sudo ./keras_GPU_support.sh
```

- - - -

# Common pitfalls
>solving failed `apt-get update` issue
```
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null
```
>resizing swap file
```
#Make all swap off
sudo swapoff -a

#Resize the swapfile
sudo dd if=/dev/zero of=/swapfile bs=9M count=1024

#Make swapfile usable
sudo mkswap /swapfile

#Make swapon again
sudo swapon /swapfile
```
