
import cv2, os
import numpy as np

maskDir = 'ds13/masks_machine'
txtDir = 'ds13/bad_img.txt'
imgList = sorted(os.listdir(maskDir))

bad = []
for name in imgList:
    img = cv2.imread(maskDir+'/'+name, 0)
    assert img is not None
    h, w = img.shape
    mask_cord = np.where(img>0)  # 2d array [[h_cord],[x_cord]]
    h_max, h_min = np.max(mask_cord[0]), np.min(mask_cord[0])
    if h>=w and (h_max - h_min)/h < 0.6:
        #print(name)
        bad.append(name)
    elif h<w and (h_max - h_min)/h < 0.45:
        #print(name)
        bad.append(name)

if bad != []:
    with open(txtDir,'w') as f:
        for name in bad[:-1]:
            f.write(name+'\n')
        f.write(bad[-1])
    print('\n',len(bad),'bad images detected!')
else:
    print('no bad image detected!')