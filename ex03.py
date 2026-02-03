# 랜덤 난수 생성 모듈 불러오기
import random

# 운영체제의 파일 핸들링 관련 기능 제공
import os
# 컴퓨터 시스템의 자원 정보 및 기능 호출
import sys

# 수학 함수
import math

# 날짜 시간 관련 기능
import datetime

import mymod as mm

print(random.randint(30,100))       # 30~100 사이 난수 1개 생성

li = random.sample(range(30,100), 5)    # 30~100 사이 난수 5개 생성해서 리스트로 반환
print(li)  
tot,avg = mm.sum_avg(li)
print(tot, avg)

li = [1,2,3,4,5,6,7,8,9,10]

random.shuffle(li)      # 리스트 값 섞기
print(li)

print(random.choice(li))    # 주어진 리스트 내에서 특정 값 하나 랜덤 추출
print(random.choices(li, k=3))    # 주어진 리스트 내에서 특정 값 k개 랜덤 추출

print(os.path.curdir)      # path 파일 경로, curdir: 현재 디렉토리
print(os.path.abspath('.'))     # 현재 파일까지 경로

# 현재 시간 출력
print(datetime.datetime.now())
cur = datetime.datetime.now()
str_cur = cur.strftime("%Y년 %m월 %d일, %H시 %M분 %S초 ")
week_str = mm.week_day_from_num(cur.strftime('%w'))
str_cur += week_str
print(str_cur)
