'''
selenium: 브라우저 등을 원격으로 제어할 수 있는 외부 모듈
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# selenium 보조 클래스
from selenium.webdriver.common.by import By     # 특정 엘리먼트를 찾을 수 있도록 도와주는 객체
from selenium.webdriver.common.keys import Keys # 
from selenium.webdriver.support.ui import WebDriverWait     # 엘리먼트가 로딩될때까지 대기하게하는 객체
from selenium.webdriver.support import expected_conditions as EC    # 로딩되어 사용할 수 있는 상태인지 체크하는 객체

def create_webdriver():
    # Options 클래스를 이용하여 options 객체 생성
    options = Options()
    # options.add_argument('--headless=new')      # 브라우저를 감춤
    options.add_argument('--disable-blink-features=AutomationControlled')      # 브라우저를 감춤
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36')
    # 컴퓨터에 설치된 크롬브라우저와 동일한 버전의 웹드라이버 설치
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def search_query_image(queary:str, web_driver):
    TIME_OUT = 10
    wait = WebDriverWait(web_driver, TIME_OUT)

    # 구글 페이지로 이동
    web_driver.get('http://www.google.com')

def main():
    query = input("검색어를 입력하세요: ")
    web_driver = create_webdriver()
    search_query_image(query, web_driver)

    time.sleep(5)

if __name__ == "__main__":
    main()


