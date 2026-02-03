'''
파이썬 모듈 만들고 사용하기
'''
# mymod 파이썬 모듈 불러오기
import mymod    # mymod에 정의된 함수들을 사용할 준비 완료
cup, rem = mymod.americano(10000)
print(f'{cup}잔,{rem}원')

total = mymod.totaler(10)
print(f'짝수: {total}')

total2 = mymod.totaler(10, False)
print(f'홀수: {total2}')
