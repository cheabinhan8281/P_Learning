'''
파이썬 모듈 만들고 사용하기
'''
# mymod 파이썬 모듈 불러오기
import mymod as mm   # mymod에 정의된 함수들을 사용할 준비 완료
# as 뒤에 키워드 별칭

cup, rem = mm.americano(10000)
print(f'{cup}잔,{rem}원')

total = mm.totaler(10)
print(f'짝수: {total}')

total2 = mm.totaler(10, False)
print(f'홀수: {total2}')
