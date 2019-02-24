
import cv2, os
import numpy as np

dir = '/media/kevin/Data/Ubuntu/bgimg_ait/'
extList = ['.jpg', '.JPG', '.jpeg', '.JPEG','.png', '.PNG', '.gif','.GIF',
           '.ppm', '.PPM', '.bmp', '.BMP', '.tiff']

i = 0
for path, subdir, files in os.walk(dir):
    for name in files:
        pre, ext = os.path.splitext(name)
        assert ext in extList
        newname = 'ait_{:05d}'.format(i)+ext
        if os.path.isfile(os.path.join(dir,path,newname)):
            print(name, newname)
            raise ValueError
        os.rename(os.path.join(dir, path, name),
                  os.path.join(dir, path, newname))
        i+=1
print('count:',i)

"""
imgList = os.listdir(dir)
assert imgList!=[]

extList = ['.jpg', '.JPG', '.jpeg', '.JPEG','.png', '.PNG', '.gif','.GIF',
           '.ppm', '.PPM', '.bmp', '.BMP', '.tiff']
i=0
for name in imgList:
    prename, ext = os.path.splitext(name)
    
    if ext !='.png' and ext in extList:
        if os.path.isfile(dir+prename+'.png'):
            #os.remove(dir+name)
            print('replicated file:',name)
        else:
            os.rename(dir+name, dir+prename+'.png')
            i+=1
    
    if ext not in extList:
        print('invalid file:', name)

#print('ext changed: ',i)
"""