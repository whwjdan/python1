# -*- coding: UTF-8 -*- 
# [ IMPORT ] #


import requests
from bs4 import BeautifulSoup
import pymysql
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass
import urllib.request
# [] #

username = ('01048293899')
password = ('a41309294')
hashTag = input("Input HashTag # : ")# Search #

checkTag = hashTag.find('#')

# [ HASHTAG USING CHECK ] #

if checkTag==-1:
    hashTag = '#'+hashTag

driver = webdriver.Chrome("C:/Users/oracle/Downloads/chromedriver.exe")# Chromedriver PATH
driver.get("https://www.instagram.com/accounts/login/")

# [ LOGIN ] #

element_id = driver.find_element_by_name("username")
element_id.send_keys(username)
element_password = driver.find_element_by_name("password")
element_password.send_keys(password)

password = 0 #RESET Password

driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > span > button').submit()
driver.implicitly_wait(5)

# [ LOGIN COMPLETE and SEARCH ] #

driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""").send_keys(hashTag)
driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""").click()

searchTotalCount = driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/header/span/span""").text
print('검색결과  Total : '+ searchTotalCount +' 건 의 게시물이 검색되었습니다.')

elem = driver.find_element_by_tag_name("body")

# [ AUTO PAGE DOWN ] #
# 자동으로 스크롤을 두번 내려줌
count = 0
while count <100:
    no_of_pagedowns = 2

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        no_of_pagedowns-=1
    count = count +1
# [ SEARCH COMPLETE ] #
# 검색하여 현재 노출된 페이지 안의 사진수 만큼의 빈 배열을 만들어둠
resultCnt = driver.find_elements_by_class_name('_2di5p')
resultValues =[]

for i in resultCnt:
    print(i.get_attribute('alt'))
    resultValues.append(i.get_attribute('alt'))
len(resultValues)
print(len(resultCnt))
resultCnt[0].get_attribute('alt')
print(resultCnt)
print(resultValues)
# 사진수 만큼의 index를 가진 빈배열 만들기 끝

wr.writerow([1, 'mkblog'])
wr.writerow([2, 'co'])
wr.writerow([3, 'kr'])
c1 = 0


f = open('output.csv', 'w', newline='', encoding='cp949')
wr = csv.writer(f)
for i in resultValues:
    c1 = c1 +1
    wr.writerow([c1, i.encoding('cp949')])
f.close()
resultValues[i]
s = '한글'
s.decode('utf-8').encode('utf-8')
u = "가나다"
b1 = u.encode("cp949")
type(b1)
b1.decode("cp949")
b2 = resultValues[0]
b2.encode('utf-8').decode('cp949')