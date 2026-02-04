'''
News API 사이트로부터 뉴스 기사 데이터를 가져와서 순서대로 출력해보기

pip : Python Package Intaller, 파이썬 외부 모듈 설치 및 관리자
<Terminal>
pip install 외부모듈명
- 내 컴퓨터에 위에 지정된 외부 모듈을 설치

requests 모듈: url을 지정하여 해당 엔드 포인트로부터 데이터를 가져옴

'''

import requests
APIKEY = 'c0e01e01172e4730bb7a62fdcca84868'
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={APIKEY}'
# print(url)

# 해당 url 서버에 요청을 보내고 응답을 받음
res = requests.get(url)
if res.status_code != 200:      # 응답코드가 200이 아니면 에러
    print('응답을 받지 못했습니다.')
    exit(-1)    # exit(n): 프로그램 즉시(비정상) 종료, exit(0): 프로그램 정상 종료
# 성공적으로 응답을 받음
# print(type(res.json()))       # 응답 객체로부터 JSON 데이터를 불러와 출력

news_data = res.json()
print(f"응답코드: {news_data['status']}")
print(f"기사개수: {news_data['totalResults']}")
print(f"실제가져온기사개수: {len(news_data['articles'])}")

# articles 리스트로부터 모든 항목 가져오기
for article in news_data['articles']:
    # 제목: ㅇㅇㅇㅇㅇㅇ
    print(f'제목: {article["title"]}')
    print(f'url: {article["url"]}')
    print(f'발행일: {article["publishedAt"]} \n발행처: {article["source"]["name"]}')