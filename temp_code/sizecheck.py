import os
import cv2
import numpy as np

sizeList = []
dir = '/media/kevin/Data/Ubuntu/bgimg_ait/coco_bg/'

allimg = os.listdir(dir)
for name in allimg:
    img = cv2.imread(dir+name)
    sizeList.append(img.shape[:2][::-1])  # (w, h)

sizeList = np.array(sizeList)
np.sort(sizeList)
print(sizeList[5000:5050])
print('\nsort by height:\n')
np.sort(sizeList.view('i8,i8,i8'), order=['f1'])
print(sizeList[5000:5050])

