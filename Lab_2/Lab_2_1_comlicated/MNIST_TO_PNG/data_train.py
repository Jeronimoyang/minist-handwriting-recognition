import numpy as np
import struct
 
from PIL import Image
import os
 
data_file = 'E:/AI_Code/Data/train-images.idx3-ubyte' #需要修改的路径

data_file_size = 47040016
data_file_size = str(data_file_size - 16) + 'B'
 
data_buf = open(data_file, 'rb').read()
 
magic, numImages, numRows, numColumns = struct.unpack_from(
    '>IIII', data_buf, 0)
datas = struct.unpack_from(
    '>' + data_file_size, data_buf, struct.calcsize('>IIII'))
datas = np.array(datas).astype(np.uint8).reshape(
    numImages, 1, numRows, numColumns)
 
label_file = 'E:/AI_Code/Data/train-labels.idx1-ubyte' #需要修改的路径
 

label_file_size = 60008
label_file_size = str(label_file_size - 8) + 'B'
 
label_buf = open(label_file, 'rb').read()
 
magic, numLabels = struct.unpack_from('>II', label_buf, 0)
labels = struct.unpack_from(
    '>' + label_file_size, label_buf, struct.calcsize('>II'))
labels = np.array(labels).astype(np.int64)
 
datas_root = 'E:/AI_Code/Data/mnist_train' #需要修改的路径
if not os.path.exists(datas_root):
    os.mkdir(datas_root)
 
for i in range(10):
    file_name = datas_root + os.sep + str(i)
    if not os.path.exists(file_name):
        os.mkdir(file_name)
 
for ii in range(numLabels):
    img = Image.fromarray(datas[ii, 0, 0:28, 0:28])
    label = labels[ii]
    file_name = datas_root + os.sep + str(label) + os.sep + \
        'mnist_train_' + str(ii) + '.png'
    img.save(file_name)