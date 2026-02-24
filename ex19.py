# 정적인 HTML 페이지로부터 데이터 저장

# requests, beautifulsoup

# 지정된 URL로부터 데이터 요청을 보내고 받는 외부 모듈
import requests
# HTML, XML, JSON 등의 포맷을 분석할 수 있는 외부 모듈
# bs4: 정적인 웹문서(HTML) 분석에 사용
from bs4 import BeautifulSoup

def make_header():
    '''크롬들의 브라우저가 하는 것처럼 request 헤더 생성'''
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    }
    return header

def requests_wiki_data():
    # Http Header 생성하여 가져옴
    header = make_header()

    url = 'https://ko.wikipedia.org/wiki/투모로우바이투게더'
    # 위 url로부터 데이터를 요청하여 res에 응답을 받음
    res = requests.get(url, headers=header, timeout=10)
    # 요청이 실패하여 응답이 정상적으로 수신되지 못한 경우 Exception 발생
    res.raise_for_status()
    # 위에서 Exception이 발생되지 않았다면, 이 지점 실행
    # print(res.text)     # 응답받은 전체 텍스트 데이터 출력
    
    # HTML 분석기와 HTML 소스코드를 전달하여 BS객체 생성
    elems = BeautifulSoup(res.text, 'html.parser')      # 텍스트 분석기
    return elems

def print_title(elems: BeautifulSoup):
    title = elems.find('h1', id='firstHeading')
    print(f'제목: {title.get_text()}')

def print_paragraph1(elems:BeautifulSoup):
    p1 = elems.find('p', id='mwBg')
    print(f'본문1: {p1.get_text()}')

# def save_image(elems:BeautifulSoup):
#     img1 = elems.find('img', class_='mw-file-element')
#     # src 속성을 가져오고 'http:' 붙여줌 
#     img_url = 'https:'+img1['src']
#     header = make_header()    # http 헤더 생성
#     res = requests.get(img_url, headers=header, timeout=10)
#     res.raise_for_status()  
#     # res.text: json 데이터나 html 소스코드 데이터 전달
#     # res.content: 이미지와 같이 binary 데이터 포함

#     # 이미지 컨텐츠 파일 저장
#     with open ('image1.jpg', 'wb') as f:
#         f.write(res.content)
#     print(img_url)

def save_image(elems: BeautifulSoup):
    # 모든 mw-file-element 이미지 가져오기
    images = elems.find_all('img', class_='mw-file-element')

    target_img = None
    for img in images:
        src = img.get('src', '')
        if 'Tomorrow_X_Together_at_a_Dior_event' in src:
            target_img = img
            break

    if not target_img:
        print("원하는 이미지를 찾을 수 없습니다.")
        return

    img_url = 'https:' + target_img['src']
    print("선택된 이미지 URL:", img_url)

    # 이미지 저장
    header = make_header()
    res = requests.get(img_url, headers=header, timeout=10)
    res.raise_for_status()

    with open('투모로우바이투게더.jpg', 'wb') as f:
        f.write(res.content)

    print("이미지 저장 완료!")

def main():
    # elems는 BS객체
    elems = requests_wiki_data()
    print_title(elems)
    print_paragraph1(elems)
    save_image(elems)

    


if __name__ == "__main__":
    main()

# requests.exceptions.HTTPError: 403 Client Error: Forbidden for url 
# 웹사이트 접근 권한 X -> 웹사이트 접근처럼 수정 make_header