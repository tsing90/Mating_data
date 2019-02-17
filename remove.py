
from selenium import webdriver
import os
import time
driver = webdriver.Chrome("C:\chromedriver.exe")

driver.get("https://www.remove.bg/")

all_cookies = driver.get_cookies()
with open('cookies.txt','w') as f:
    f.write(str(all_cookies))
print (all_cookies)

#driver.add_cookie({})
#driver.find_element_by_link_text("Select a photo").click()

#time.sleep(1)

#os.system(r'D:\Research_Imperial\GitHub\matting_data\upload.exe "D:\Research_Imperial\GitHub\matting_data\test.jpg"')
#time.sleep(5)
driver.quit()






""" using win32gui / focus switch

import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import win32gui
import win32con

chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()


driver.get("https://www.remove.bg/")
driver.find_element_by_link_text("Select a photo").click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    print('no pop-up window after 10s, exit!')
    driver.quit()
driver.find_element_by_name("image[original]").clear()
driver.find_element_by_name("image[original]").send_keys("/home/kevin/git/matting_data/dili.png")
driver.find_element_by_link_text("Download").click()
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
driver.close()


"""

"""
import requests


s = requests.session()
headers = {
    'Host': 'https://www.remove.bg',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
    'Accept-Encoding':'gzip, deflate, br',
}
proxies = {'http': 'http://167.99.204.234',   'https': 'https://185.112.249.33'}

file = {'uploadFile': open('./dili.png', 'rb')}
r = s.post('https://www.remove.bg/#', headers=headers, files=file)

print(r.content)

"""



"""  spider
import urllib2
import os
import scrapy


class GetMat(scrapy.Spider):
    name = 'test'
    start_urls = ['https://www.remove.bg/',]

    def parse(self, response):




div upload-list-wrapper
"""