import requests
import os

APIKEY = 'c0e01e01172e4730bb7a62fdcca84868'

def show_menu():
    '''프로그램의 메인 메뉴를 보여주는 함수'''
    os.system('cls')        # 커맨더 라인 명령어 실행

    print("1. 경제 뉴스")
    print("2. 연예 뉴스")
    print("3. 생활 건강 뉴스")
    print("4. 순수 과학 뉴스")
    print("5. 스포츠 뉴스")
    print("6. 최신 기술 뉴스")
    print("====================")
    print("x. 프로그램 종료")

def select_menu():
    
    while True:
        menu = input("메뉴 번호를 입력하세요: ")
        match(menu):
            case '1'|'2'|'3'|'4'|'5'|'6':
                return menu
            case 'x':
                print("프로그램을 종료합니다.")
                exit(0)         # 프로그램 즉시 종료
            case _: print("메뉴를 잘 못 입력했습니다.")

def select_category(menu):
    match(menu):
        case '1': return 'business'
        case '2': return 'entertainment'
        case '3': return 'health'
        case '4': return 'science'
        case '5': return 'sports'
        case '6': return 'technology'

def get_news_data(category:str):
    '''전달받은 category를 이용하여 url을 만들고 뉴스 서버에 요청 보냄'''
    # 해당 카테고리의 데이터를 요청하는 url
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={APIKEY}'
    # 뉴스 서버에 요청 보냄
    res = requests.get(url)
    if res.status_code!=200:
        print("요청에 실패했습니다. url을 확인하세요...")
        return None
    # 응답 데이터의 최상위 딕셔너리 데이터
    res_data = res.json()    
    if res_data['status'].lower() != 'ok':
        print("요청에 실패했습니다. 응답코드를 확인하세요...")
        return None
    # 성공
    return res_data['articles']

# 뉴스 기사 데이터를 입력으로 하는 함수 정의
def show_articles(articles:list):
    for article in articles:
        # 제목: ㅇㅇㅇㅇㅇㅇ
        print(f'제목: {article["title"]}')
        print(f'url: {article["url"]}')
        print(f'발행일: {article["publishedAt"]} \n발행처: {article["source"]["name"]}')

if __name__ == "__main__":
    while True:
        # 이 부분부터 프로그램이 실행됨
        show_menu()
        menu = select_menu()                # 메뉴 선택
        category = select_category(menu)    # 메뉴 전달, 카테고리명
        articles = get_news_data(category)  # 뉴스 기사 데이터 리스트 객체 전달받음
        show_articles(articles)
        respond = input("계속하려면 엔터를 입력하세요. ")
        if respond != '':
            break

