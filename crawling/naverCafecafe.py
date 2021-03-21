from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


driver = webdriver.Chrome('C:/Users/oracle/Downloads/chromedriver.exe')
driver.implicitly_wait(3)

# 로그인 전용 화면
driver.get('https://nid.naver.com/nidlogin.login')
# 아이디와 비밀번호 입력
driver.find_element_by_name('id').send_keys('whwjdan')
driver.find_element_by_name('pw').send_keys('a41309294')
# 로그인 버튼 클릭22
driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()
driver.get('http://cafe.naver.com/sssw')
driver.get('http://www.naver.com')

time.sleep(2)
driver.find_element_by_css_selector('#menuLink130').click()
driver.find_element_by_xpath("""//*[@id="cafe-menu"]/""")
# 메인화면 완료
#menuLink351
#menuLink429
#u_skip
#menuLink374
//*[@id="menuLink374"]
#special-menuLink-0
# "http://cafe.naver.com/ArticleList.nhn?search.clubid=10625158&search.menuid=130&search.boardtype=I"
"http://cafe.naver.com/ArticleList.nhn?search.clubid=10625158&search.boardtype=L"

base_url1 = "http://cafe.naver.com/ArticleList.nhn?search.clubid=10625158&search.boardtype=L"
base_url = 'http://cafe.naver.com/ArticleList.nhn?search.clubid=10625158'
# driver.get(base_url)
print(driver.find_element_by_class_name('gm-tcol-t'))
driver.get(base_url1)
driver.get(base_url + '&search.menuid=130&search.boardtype=I')

#

driver.switch_to_frame(driver.find_element_by_id("cafe_main"))
driver.find_element_by_xpath("""//*[@id="main-area"]/div[4]""")
driver.find_element_by_id("cafe_main")
driver.switch_to_frame("cafe-main")
driver.find_element_by_css_selector("#special-menuLink-0")
driver.find_element_by_xpath("""//*[@id="main-area"]/div[4]""")
driver.find_element_by_css_selector()
# iframe으로 프레임 전환
###테스트
//*[@id="main-area"]/div[6]/form/table/tbody/tr[1]/td[2]/span/span[2]










###

# href 속성을 찾아 url을 리스트로 저장한다.
#main-area > ul.article-album-sub.border-sub > li:nth-child(1) > dl > dt > a
driver.get("http://cafe.naver.com/ArticleList.nhn?search.clubid=29308320&search.menuid=1&search.boardtype=L")
driver.switch_to_frame(driver.find_element_by_id("cafe_main"))
article_list = driver.find_elements_by_css_selector('dl > dt > a.m-tcol-c')
article_list = driver.find_elements_by_css_selector('td.board-list > span > span > a.m-tcol-c')
article_urls = [ i.get_attribute('href') for i in article_list ]
print(article_list)
print(article_urls)
## url 불러옴    코드 수정 dl>a.m-tol-c          >> dl>dt>a
#main-area > ul.article-album-sub.border-sub > li:nth-child(1) > dl > dt > a.m-tcol-c.width_comment

res_list = []
# Beautifulsoup 활용
count = 0

###### def 종료####def crawl(article_urls):
    # Beautifulsoup 활용
    count = 0

defUrl =  "http://cafe.naver.com/ArticleList.nhn?search.clubid=29308320&search.boardtype=L"
defUrl = base_url + '&search.menuid=351&search.boardtype=I'
driver.get(defUrl)
driver.switch_to_frame(driver.find_element_by_id("cafe_main"))
article_list = driver.find_elements_by_css_selector('dl > dt > a.m-tcol-c')
article_list = driver.find_elements_by_css_selector('td.board-list > span > span > a.m-tcol-c')
print(article_list)
article_urls = [ i.get_attribute('href') for i in article_list ]
res_list = []
def crawl(article_urls):
    count = 0
    if(count <15):
        for article in article_urls:
            count = count +1
            driver.get(article)
            try:
                time.sleep(1)
                driver.switch_to.alert.accept()
                print('Alarm! ALARM!')
            except Exception as e:
                time.sleep(1)
        # article도 switch_to_frame이 필수
        driver.switch_to_frame('cafe_main')
        soup = bs(driver.page_source, 'html.parser')
        # 제목 검색
        title = soup.select('div.tit-box span.b')[0].get_text()
        # 게시글을 띄어쓰기 단위로 합친다.
        content_tags = soup.select('#tbody')[0].select('p')
        content = ' '.join([tags.get_text() for tags in content_tags])
        # dict형태로 만들어 결과 list에 저장
        res_list.append({'title': title, 'content': content})
    else:
        print('16')
    driver.get(defUrl)

crawl( article_urls)
res_list
    # time.sleep 작업도 필요하다.
driver.get('http://cafe.naver.com/ArticleRead.nhn?clubid=10050146&page=1&boardtype=L&articleid=446626322&referrerAllArticles=true')
alert = driver.switch_to_alert()
alert.dismiss()
driver.find_element_by_css_selector('alert')
# 결과 데이터프레임화
cafe_df = pd.DataFrame(res_list)
print(cafe_df)
# csv파일로 추출
cafe_df.to_csv('cafe_crawling.csv', index=False)



###### exception test########
try:
    driver.get('http://cafe.naver.com/ArticleRead.nhn?clubid=29308320&page=1&boardtype=L&articleid=4&referrerAllArticles=true')
    # driver.get("http://cafe.naver.com/ArticleList.nhn?search.clubid=29308320&search.boardtype=L")
    time.sleep(2)
    driver.switch_to.alert.accept()
except Exception as e:
    print('exception 발생')
    print(Alert.text)



try:
    driver.switch_to.alert.accept()
    print('Alarm! ALARM!')
except NoAlertPresentException:
    print('*crickets*')
############################## Exception test#################################