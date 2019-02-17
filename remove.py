
import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()


driver.get("https://www.remove.bg/")
driver.find_element_by_link_text("Select a photo").click()
time.sleep(1)
driver.find_element_by_name("image[original]").clear()
driver.find_element_by_name("image[original]").send_keys("/home/kevin/git/matting_data/dili.png")
driver.find_element_by_link_text("Download").click()
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
driver.close()





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



"""
import urllib2
import os
import scrapy


class GetMat(scrapy.Spider):
    name = 'test'
    start_urls = ['https://www.remove.bg/',]

    def parse(self, response):




div upload-list-wrapper
"""