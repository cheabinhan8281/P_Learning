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
from selenium.webdriver.common.keys import Keys # 키보드 제어
from selenium.webdriver.support.ui import WebDriverWait     # 엘리먼트가 로딩될때까지 대기하게하는 객체
from selenium.webdriver.support import expected_conditions as EC    # 로딩되어 사용할 수 있는 상태인지 체크하는 객체

TIME_OUT = 10

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
    try:
        # 엘리먼트가 나타날 때까지 기다리게 해주는 객체
        wait = WebDriverWait(web_driver, TIME_OUT)

        # 구글 페이지로 이동
        web_driver.get('http://www.google.com')
        
        # 검색어 입력창 찾음
        search_box = wait.until(
            # 클릭 가능한 엘리먼트 중에서
            EC.element_to_be_clickable((By.CSS_SELECTOR,"textarea[name='q']"))
        )

        search_box.click()                  # 검색어 입력창 클릭 -> 포커스를 준다
        search_box.send_keys(queary)        # 입력한 검색어를 검색어창에 넣어준다
        search_box.send_keys(Keys.ENTER)    # 엔터키를 친다

        # 이미지 탭을 찾아서 이미지 탭을 클릭하여 이미지 검색 페이지로 이동
        image_tab = wait.until(
        # 클릭 가능한 엘리먼트 중에서
            EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='udm=2']"))
        )
        image_tab.click()   

        # 이미지 썸네일들을 포함하고 있는 Grid 엘리먼트가 나타났는지 체킹하고 기다림
        return wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"div[data-id*='mosaic']"))
        )
    except Exception as e:
        print(f"이미지 검색 중 에러 발생: {e}")
        return None

def get_image_urls(imgs_grid, web_driver, num_images=10):
    '''이미지 그리드에 나타난 썸네일들로부터 이미지 원본의 url을 추출하여 반환'''
    urls = []
    all_links = imgs_grid.find_elements(By.TAG_NAME, 'a')
    print(f"링크들의 개수: {len(all_links)}")
    thumbnails = []     # 썸네일 url들이 저장될 리스트
    for link in all_links:
        href = link.get_attribute('href')
        if not href:
            imgs = link.find_elements(By.TAG_NAME, 'img')
            if imgs and imgs[0].size.get('width', 0) > 100:
                thumbnails.append(link)
    print(f'링크들의 개수: {len(thumbnails)}')

    # 썸네일들을 하나씩 클릭한다
    for thumb in thumbnails:
        if len(urls) >= num_images:
            break
        try:
            thumb.click()       # 썸네일 클릭
            wait = WebDriverWait(web_driver, TIME_OUT)
            wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img[jsname='kn3ccd']"))
            )

            def original_image_loaded(driver):
                imgs = driver.find_elements(By.CSS_SELECTOR, "img[jsname='kn3ccd']")
                for img in imgs:
                    src = img.get_attribute('src')
                    if src and src.startswith('http') and 'encrypted' not in src:
                        return src
                return False
            src = wait.until(original_image_loaded)
            if src not in urls:
                urls.append(src)
                print(f'{len(urls)}개 수집함...')

        except Exception as e:
            print(f'오류가 발생하여 스킵합니다.')
    


def main():
    query = input("검색어를 입력하세요: ")
    web_driver = create_webdriver()
    imgs_grid = search_query_image(query, web_driver)
    get_image_urls(imgs_grid, web_driver)



    time.sleep(5)

if __name__ == "__main__":
    main()


