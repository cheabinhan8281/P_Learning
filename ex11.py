li = [10,20,30,40,50]
print(li)

while True:
    index = int(input('선택하고자 하는 숫자의 인덱스를 입력하세요: '))
    try:
        print(f'선택한 숫자는 {li[index]}입니다.')
        
    except IndexError as e:
        print('숫자 인덱스를 입력해주세요.')
        print(f'에러 메세지: {e}')
        print('다시 입력하세요.')
    except TypeError:
        print('지원되지 않는 타입의 데이터를 선택했습니다.')
        print(f'에러 메세지: {e}')
        print('다시 입력하세요.')
    except RuntimeError:
        print('에러')
    except Exception as e:
        # 어떤 에러가 발생할지 모르지만, 정상 작동
        print('알 수 없는 에러가 발생했습니다.')
        print(f'에러 메세지: {e}')