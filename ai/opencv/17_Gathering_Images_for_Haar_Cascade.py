import urllib.request
import cv2
import numpy as np
import os


pos_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02708433'
neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'


def store_raw_images(images_link, state, pic_num):
    image_urls = urllib.request.urlopen(images_link).read().decode()
    if not os.path.exists(state):
        os.makedirs(state)

    for i in image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, state + "/" + str(pic_num) + ".jpg")
            img = cv2.imread(state + "/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            if state == 'pos':
                resized_image = cv2.resize(img, (50, 50))
            else:
                resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite(state + "/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))
    return pic_num
#we will use only one positive image to train with, if we want to train with 5000 images, then we should have 25000 neg images
#last_pic_num = store_raw_images(pos_images_link, 'pos', 1)
#store_raw_images(neg_images_link, 'neg', last_pic_num)


######################

#create uglies directory with sample of empty image of dimensions 50x50 and 100x100,
# and change the string in this function to be once 'pos' and once 'neg'
def find_uglies():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))
#find_uglies()


######################

def create_pos_n_neg():
    for file_type in ['neg']:

        for img in os.listdir(file_type):

            if file_type == 'pos':
                #description file, contain number of objects to detect, rectangle dimensions to look in
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)
create_pos_n_neg()


######################

def change_img_size():
    for img_name in os.listdir("neg"):
        try:
            img = cv2.imread("neg/"+str(img_name))
            resized_image = cv2.resize(img, (50, 50))
            #you should create pos/ directory first
            cv2.imwrite("pos/" + str(img_name), resized_image)
            print("pos/" + str(img_name))

        except Exception as e:
            print(str(e))
#change_img_size()


######################

#to rename images in a directory
def neg_corrected():
    cntr = 567
    for img_name in os.listdir("neg"):
        try:
            img = cv2.imread("neg/"+str(img_name))
            cv2.imwrite("neg_c/" + str(cntr) + ".jpg", img)
            print("neg_c/" + str(cntr) + ".jpg")
            cntr+=1

        except Exception as e:
            print(str(e))

#neg_corrected()