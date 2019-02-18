
from selenium import webdriver
import os
import time, winsound
import argparse

parser = argparse.ArgumentParser(description='dataset preparing script')
parser.add_argument('--image', '-i', default='image', help='source image dir')
parser.add_argument('--alpha', '-a', default='alpha', help='output alpha dir')
args = parser.parse_args()
imgDir = os.path.join("D:\git\matting_data", args.image)
outDir = os.path.join("D:\git\matting_data", args.alpha)
print('input dir:',imgDir,'\noutput:',outDir)

profile_dir = r'C:\Users\ic_lc2015\AppData\Local\Google\Chrome\ForCrawl'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))

driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path="C:\chromedriver.exe")

driver.get("https://www.remove.bg/")
time.sleep(5) # make sure the website is fully loaded

imgList = sorted(os.listdir(imgDir))
for name in imgList:
    if os.path.isfile(os.path.join(outDir, name[:-4]+'.png')):
        continue

    driver.find_element_by_link_text("Select a photo").click()
    time.sleep(2)

    imgPath = os.path.join(imgDir, name)
    try:
        os.system(r'D:\git\matting_data\upload.exe {}'.format(imgPath))
    except:
        print('Uploading problem  ...')
        times = 15
        for i in range(times):
            winsound(440, 1000)  # beep for 1s
            time.sleep(5)
            print((times-1-i)*6, 'seconds left!')
        os.system(r'D:\git\matting_data\upload.exe {}'.format(imgPath))

    time.sleep(20)  # website image processing

    #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Regular'])[1]/following::span[1]").click()
    driver.find_element_by_link_text("Download").click()
    time.sleep(2)

    outPath = os.path.join(outDir, name[:-4]+'.png')
    try:
        os.system(r'D:\git\matting_data\save_as.exe {}'.format(outPath))
        time.sleep(2)
    except:
        print('Downloading problem ...')
        times = 10
        for i in range(times):
            winsound(440, 1000)  # beep for 1s
            time.sleep(5)
            print((times-1-i)*6, 'seconds left!')
        os.system(r'D:\git\matting_data\upload.exe {}'.format(outPath))
        time.sleep(2)
    print('Downloaded alpha image:', name[:-4]+'.png')

driver.quit()
