import json
import requests
from bs4 import BeautifulSoup 
import driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import codecs


driver = webdriver.Chrome()
#driver.get("https://www.facebook.com/%E5%8F%AA%E6%98%AF%E5%A0%B5%E8%97%8D-245311342852891/")
#driver.get("https://www.facebook.com/XieLiSheng/")
#driver.get("https://www.facebook.com/ROC.Blue.Power/?ref=page_internal")
driver.get("https://zh-tw.facebook.com/people/%E5%8F%8D%E8%94%A1%E8%8B%B1%E6%96%87%E7%B2%89%E7%B5%B2%E5%9C%98/100064877342886/")
#滑
for x in range(300):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #print("滑")
    time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# 定位文章標題
titles = soup.find_all("div", class_="x78zum5 xdt5ytf xz62fqu x16ldp7u")
#csv寫入
csv_writer = csv.writer(codecs.open('BLUE-2.csv', 'w', 'utf-8'))
for title in titles:
    posts = title.find_all("div", dir="auto")
    if len(posts):
        for post in posts:
            csv_writer.writerow([0,post.text])
