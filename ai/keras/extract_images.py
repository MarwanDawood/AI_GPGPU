from shutil import copyfile
import os


path = '/home/marwan/Desktop/raspberry/AI/keras/VOCdevkit/VOC2012/'
target = '/home/marwan/Desktop/raspberry/AI/keras/VOCdevkit/VOC_sample/'
target_ann = '/home/marwan/Desktop/raspberry/AI/keras/VOCdevkit/VOC_sample/Annotations/'
target_img = '/home/marwan/Desktop/raspberry/AI/keras/VOCdevkit/VOC_sample/JPEGImages/'

#compare images found in text file, copy them and their xml anootaion files to another folder
def extract_images(images_link):

    #check if source directory exists
    if not os.path.exists(path):
	print 'error: path not found'
	return -1

    #check if destination directory exists
    if not os.path.exists(target):
        os.makedirs(target)
        os.makedirs(target + 'ImageSets/')
        os.makedirs(target + 'ImageSets/Main/')
        os.makedirs(target_ann)
        os.makedirs(target_img)
	# create an empty file.
	try:
	    f = open(target + 'ImageSets/Main/trainval.txt', 'w')
	    f.close()
	    f = open(target + 'ImageSets/Main/test.txt', 'w')
	    f.close()
	except IOError:
	    print "Wrong path provided"

    #read all lines in this file
    with open(path + 'final_pos.txt', 'rb') as f:
	f_content = f.read()

    #create the destination file paths and copy them
    for i in f_content.split('.xml\n'):
        try:
	    ann = path + 'Annotations/' + i + '.xml'
	    img = path + 'JPEGImages/' + i + '.jpg'
 	    print img

	    copyfile(ann, target_ann + i + '.xml')
	    copyfile(img, target_img + i + '.jpg')

        except Exception as e:
            print(str(e))
    return 1


pic_num = extract_images(path)

