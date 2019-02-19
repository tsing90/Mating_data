import os
import shutil


allimg = os.listdir('new')
src = '/home/kevin/git/Deep Image Matting/Deep-Image-Matting/Combined_Dataset/Training_set/Other/alpha/'

for name in allimg:
    shutil.move(src + name, '/home/kevin/git/matting_data/DIM/alpha/')
