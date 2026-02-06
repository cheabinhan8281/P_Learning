'''
GEO code request url
http://api.openweathermap.org/geo/1.0/direct?q=성남시,KR&limit=&appid=b0def4f724cfb0404a64afc89ab26618

current weather data request url
https://api.openweathermap.org/data/2.5/weather?units=metric&lat={lat}&lon={lon}&appid={APIkey}
https://api.openweathermap.org/data/2.5/weather?units=metric&lat=37.4201556&lon=127.1262092&appid=b0def4f724cfb0404a64afc89ab26618

'''

import requests

APIKEY = 'b0def4f724cfb0404a64afc89ab26618'

# 지역의 위도, 경도 정부 가져오기
# res = requests.get('http://api.openweathermap.org/geo/1.0/direct?q=성남시,KR&limit=&appid=b0def4f724cfb0404a64afc89ab26618')
# print(res.json())

def get_geocode(city:str, apikey:str='b0def4f724cfb0404a64afc89ab26618', country_code:str='kr'):
    '''
    도시이름, APIKEY, 국가코드를 입력받아 해당 도시의 위도(lat), 경도(lon) 반환
    Args:
        city: 도시이름
        apikey: openweathermap api key
        country_code: 국가코드, 기본값은 kr

    Returns:
        lat(위도), lon(경도)
    '''
    
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&limit=&appid={apikey}'
    res = requests.get(url)             # geocode 서버에 요청
    if res.status_code != 200:          # http 요청 시 에러 발생 확인
        print("GEO 코드 요청 실패")
        return None, None
    # 응답 데이터
    res_data = res.json()               # 응답 데이터 JSON(리스트+딕셔너리)
    if len(res_data) == 0:
        print("지역명을 다시 입력하세요")
        return None, None
    # 성공
    geo_data =  res_data[0]
    lat = geo_data['lat']
    lon = geo_data['lon']
    return lat, lon
    
def get_current_weather(lat:float,lon:float,apikey:str='b0def4f724cfb0404a64afc89ab26618') -> dict|None:
    '''
    위, 경도를 받아서 현재 그 지역의 날씨 정보를 요청하고 반환
    Args:
        lat: 위도
        lon: 경도
        apikey: Open Weather Map Api Key
        
    Returns:
        날씨 정보, 타입은 dict
    '''
    url = f'https://api.openweathermap.org/data/2.5/weather?units=metric&lat={lat}&lon={lon}&appid={apikey}'
    res = requests.get(url)     # 현재 날씨 정보
    if res.status_code != 200:
        print('Current weather 데이터 요청 실패')
        return None
    # 응답 코드 확인하기
    res_data = res.json()
    if res_data['cod'] != 200:
        print("잘못된 요청입니다. 위도, 경도, APIKEY를 확인하세요")
        return None
    return res_data

def show_main_weather(cur_weather:dict):
    weather = cur_weather["weather"][0]
    print(weather)
    print(f'날씨: {weather["main"]}')

def show_temp(cur_weather:dict):
    temperature = cur_weather["main"]
    print(temperature)
    print(f'기온: {temperature["temp"]}')
    print(f'습도: {temperature["humidity"]}')
    print(f'기압: {temperature["pressure"]}')

def show_wind(cur_weather:dict):
    wind = cur_weather["wind"]
    print(wind)
    print(f'풍속: {wind["speed"]}')
    print(f'방향: {wind["deg"]}')

def show_time(cur_weather:dict):
    time = cur_weather["sys"]
    print(time)
    print(f'관측시간: {cur_weather["dt"]}')
    print(f'일출시간: {time["sunrise"]}')
    print(f'일몰시간: {time["sunset"]}')

    

# 프로그램의 시작점 만들기

if __name__ == '__main__':
    while True:
        city = input("지역을 입력하세요(x입력시 종료): ")
        if city == 'x':
            print("프로그램 종료")
            exit(0)
        

        lat, lon = get_geocode(city)
        if lat is None or lon is None: continue
        get_current_weather(lat,lon,APIKEY)

        cur_weather = get_current_weather(lat,lon)
        if cur_weather is None: continue

        show_main_weather(cur_weather)
        show_temp(cur_weather)
        show_wind(cur_weather)
        show_time(cur_weather)


# 지역을 입력하세요: 
# 현재 날씨: 
# 설명: 
# 기온:
# 체감 기온:
# 최저 기온:
# 최고 기온:
# 습도: 
# 기압:
# 풍속:
# 풍향:
# 관측 시간:
# 해뜨는 시간: 
# 해지는 시간: 