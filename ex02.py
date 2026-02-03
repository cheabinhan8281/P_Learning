'''모듈에서 필요한 기능만 불러오기(나머지 공간 낭비)'''
# from 모듈명 import 함수1,함수2...함수n
from mymod import americano, calculator as calc     # totaler 사용 불가
cup, rem = americano(10000)
print(f'{cup}잔,{rem}원')

res = calc(10, '*', 3)
print(res)
res2 = calc(5, '-', 9)
print(res2)

# 파이썬 기본 패키지 함수들
'''
print(), input(), len(), max(), sum()
'''
print(sum([1,2,3]))     # sum() 반복 가능한(iterable) 객체의 합
print(max(1,2,3,4,5))   # 전달된 값들 중 최댓값
print(min(1,2,3,4,5))   # 전달된 값들 중 최솟값
print(divmod(10,3))     # 몫,나머지 반환
print(eval('10*3'))     # 문자열 실제 계산 출력
