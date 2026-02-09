'''
객체 지향 프로그래밍 (속성/메소드)

객체(Object): 여러가지 속성을 가지는 모든 대상
현실 세계의 사물을 추상화하여 프로그래밍 코드로 표현하는 데 사용되는 중요한 개념.
단순 데이터를 저장하는 변수와 달리 데이터와 행동을 함께 표현해 현실 세계를 더욱 정확히 반영.
# 객체의 주요 특징
- 상태(state): 객체는 데이터와 상태를 가짐. ex.학생; 이름, 나이, 학과 등
- 행동(behavior): 객체는 특정 기능이나 행동 수행 가능. ex.공부, 독서

클래스
객체를 만드는 하나의 틀. 객체의 설계도 역할을 하여, 객체를 일관되고 효율적으로 관리.

# 클래스 정의
class 클래스명:
    클래스_변수
    생성자
    메서드

self: 객체 자신을 가리키는 특별한 변수로, 메서드 내 객체 속성이나 다른 메서드에 접근하고 변경하는 데 사용. 파이썬이 자동으로 넣어주는 변수.
메서드(method): 클래스가 가진 함수
'''
import os

class Person:
    def introduce(self, name):    # 생성자
        self.name = name
        print(f"안녕하세요. 저는 {name}입니다.")

minsu = Person()
minsu.introduce('민수')

class Animal:
    def cry(self, sound):
        self.sound = sound
        print(f"저의 울음 소리는 {sound}입니다.")

cat = Animal()
cat.cry('야옹')
print(cat.sound)
dog = Animal()
dog.cry('멍멍')
print(dog.sound)

# os.system('cls')

'''
생성자(constructor)
# 특징
- 기본 생성자(내용, 매개변수가 비어있는 생성자)는 별도 코드 없이 자동 생성
- 객체 생성 시 자동 호출
- 생성자를 선언할 때와 호출할 때 서로 다른 이름 사용
  생성자 선언: __init__() 
  생성자 호출: 클래스()
'''
class Person():
    # initialize
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"안녕하세요. 저는 {self.name}입니다.")

minsu = Person('minsu')
minsu.introduce()

class Animal():
    def __init__(self, sound):
        self.sound = sound
    def cry(self):
        print(self.sound*2)
    def __del__(self):
        print(self.sound, '객체 소멸')
cat = Animal('야옹')
cat.cry()
dog = Animal('멍')
dog.cry()
del(cat, dog)

'''
소멸자: 객체 소멸 시 호출되는 메소드로, 기본적으로 존재하며 별도 선언 없이 사용 가능.
        (객체가 더이상 사용되지 않고 메모리에서 제거되기 전 마지막으로 수행되는 코드)
- 선언: __del__()
- 호출: del 클래스명
'''
class Cup:
    def __init__ (self, color, brand):
        self.color = color
        self.brand = brand
    def __del__ (self):
        print(self.brand, '컵 객체가 소멸되었습니다.')

starCup = Cup('초록','스타벅스')
print(f'컵 색깔: {starCup.color}, 브랜드: {starCup.brand}')
del(starCup)
angelCup = Cup('금색','엔젤리너스')
print(f'컵 색깔: {angelCup.color}, 브랜드: {angelCup.brand}')
del(angelCup)

os.system('cls')

'''
클래스 변수: 클래스 안에 공간이 할당된 변수로 해당 클래스에 속한 모든 객체들이 공유하는 변수
'''
class Student:
    subject = '미술'    # 클래스 변수 선언
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f'안녕하세요. {self.name}입니다.')
        print(f'1교시 수업은 {self.subject}입니다.')
    def subject_intro(self):
        print(f'저는 {self.name}입니다.')
        if self.subject == Student.subject:
            print(f'1교시 수업은 예정대로 {Student.subject}입니다.')
        else:
            print(f'1교시 수업이 변경되어 {self.subject}입니다.')
han = Student('채빈')
chae = Student('chae')
han.introduce()
han.subject_intro()
chae.subject_intro()

# 클래스 변수 변경 및 사용
Student.subject = '수학'
print("--전체 변경--")
han.subject_intro()
chae.subject = '국어'
chae.subject_intro()

'''
클래스 변수 접근 방식
1.클래스.변수명
모든 객체에 영향을 미치는 클래스 변수 값 변경
2.객체.변수명
특정 객체에 영향을 미치는 클래스 변수 값만 변경
'''

