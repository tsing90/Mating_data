
import os

root = '/media/kevin/Data/Ubuntu/bgimg_ait/'
imgList = []

i=0
for path, subdir, files in os.walk(root):
    for name in files:
        imgList.append(os.path.join(root,path,name))
        i+=1
print('total count:',i)
imgList.sort()
with open('bg_list.txt','w') as f:
    for name in imgList[:-1]:
        f.write(name+'\n')
    f.write(imgList[-1])
