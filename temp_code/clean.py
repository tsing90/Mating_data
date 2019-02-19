
import os

imgDir = 'ds13/img'
maskDir = 'ds13/masks_machine'
txtDir = 'ds13/bad_img.txt'
with open(txtDir,'r') as f:
    for name in f.readlines():
        try:
            os.remove(imgDir+'/'+name.strip())
        except FileNotFoundError:
            os.remove(imgDir+'/'+name.strip()[:-4]+'.jpg')
        os.remove(maskDir+'/'+name.strip())

print('all cleaned')
