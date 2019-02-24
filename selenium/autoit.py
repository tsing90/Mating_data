
import os
import time, winsound
import argparse
import tqdm

parser = argparse.ArgumentParser(description='dataset preparing script')
parser.add_argument('--image', '-i', default='image', help='source image dir')
parser.add_argument('--alpha', '-a', default='alpha', help='output alpha dir')
args = parser.parse_args()
imgDir = os.path.join("D:\git\matting_data", args.image)
outDir = os.path.join("D:\git\matting_data", args.alpha)
print('input dir:',imgDir,'\noutput:',outDir)

imgList = sorted(os.listdir(imgDir))
print('Going to start: 5s ...')
time.sleep(5)
for name in tqdm.tqdm(imgList):
    if os.path.isfile(os.path.join(outDir, name[:-4]+'.png')):
        continue

    imgPath = os.path.join(imgDir, name)
    upload = True
    time.sleep(5)
    while upload:
        try:
            os.system(r'D:\git\matting_data\upload.exe {}'.format(imgPath))
            upload = False
        except:
            print('Uploading problem  ...')
            winsound(440, 1000)  # beep for 1s
            time.sleep(10)

    outPath = os.path.join(outDir, name[:-4]+'.png')
    download = True
    time.sleep(5)
    while download:
        try:
            os.system(r'D:\git\matting_data\save_as.exe {}'.format(outPath))
            download = False
        except:
            print('Downloading problem ...')
            winsound(440, 1000)  # beep for 1s
            time.sleep(10)
    #print('Downloaded alpha image:', name[:-4]+'.png')
