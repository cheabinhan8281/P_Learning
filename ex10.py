'''
예외 처리
Error(Exception)
1. Syntax Error: 문법 에러
2. Runtime Error: 실행 중에 발생하는 에러
3. Logical Error
'''
while True:
    try:
        num1 = int(input('첫번째 정수를 입력하세요 >>> '))
        num2 = int(input('두번째 정수를 입력하세요 >>> '))
        print(num1+num2)
        print(num1-num2)
        print(num1*num2)
        print(num1/num2)
        break

    except ValueError as e:
        print('잘못된 값을 입력했습니다.')
        print(f'에러 메시지: {e}')
    except ZeroDivisionError as e:
        print('0으로 나누는 시도를 했습니다.')
        print('처리할 수 없으니 다시 입력하세요.')
        print(f'에러 메시지: {e}')