
from selenium import webdriver
import os
import time, winsound

profile_dir = r'C:\Users\ic_lc2015\AppData\Local\Google\Chrome\ForCrawl'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))

driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path="C:\chromedriver.exe")

driver.get("https://www.remove.bg/")


driver.find_element_by_link_text("Select a photo").click()
time.sleep(2)

try:
    os.system(r'D:\git\matting_data\upload.exe "D:\git\matting_data\image\1.jpg"')
    time.sleep(20)
except:
    print('Uploading problem  ...')
    for i in range(10):
        winsound(440, 1000)  # beep for 1s
        time.sleep(5)
        print((9-i)*6, 'seconds left!')
    os.system(r'D:\git\matting_data\upload.exe "D:\git\matting_data\image\1.jpg"')
    time.sleep(20)

driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Regular'])[1]/following::span[1]").click()
time.sleep(2)

try:
    os.system(r'D:\git\matting_data\save_as.exe "D:\git\matting_data\alpha\1.jpg"')
    time.sleep(2)
except:
    print('Downloading problem ...')
    for i in range(10):
        winsound(440, 1000)  # beep for 1s
        time.sleep(5)
        print((9-i)*6, 'seconds left!')
    os.system(r'D:\git\matting_data\upload.exe "D:\git\matting_data\image\1.jpg"')
    time.sleep(2)

driver.quit()
