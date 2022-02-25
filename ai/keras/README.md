This work is built based on [faster RCNN](https://github.com/yhenon/keras-frcnn)
- - - 
# Useful to install to view pixel coordinates
'pip install matplotlib'

# Preparing the data
Searching for some text in files in a folder, then extracting this text

#search for a word in files
```
ack bus > pos.txt
```
#w to search using regex
#o to output only matching regex pattern
```
ack -wo .*\.xml pos.txt > final_pos.txt
```
#search for files
```
find ../ -name '*001044*'
```

# Preparing the CNN
* in file `pascal_voc_parser.py`, change the input for `data_paths` to contain only the directories you want to train it with
* the file `resnet50_weights_tf_dim_ordering_tf_kernels.h5` has the weights of a pretrained network, however, to make this network work, you have to provide it again with different images and annotations and after training (normally, 1 epoch can take 5 hours running on CPU only and depending on your machine)
* after running this, it will generate `model_frcnn.hdf5` which can be used to test and detect objects for your neural network.

## Training CNN
```
python train_frcnn.py -p /home/marwan/Desktop/raspberry/AI/keras/VOCdevkit/ -o VOC_sample --num_epochs 5
```
## Testing CNN
```
python test_frcnn.py -p /home/marwan/Desktop/raspberry/AI/keras/VOCdevkit/test/
```