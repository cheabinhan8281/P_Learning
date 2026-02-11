class AgeException(Exception):      # 에러 정의
    def __init__(self, *args):
        super().__init__(*args)

class NameException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class Person:
    def __init__(self,name,age):
        if name == '':
            raise NameException('이름은 빈칸이 할당될 수 없습니다.')
        self.__name = name
        if age < 0:     # self.age = age 대입하기 전에 조건 세워주기!
            raise AgeException('나이는 음수가 할당될 수 없습니다')
        self.__age = age
        self.__parent = '부모님'        # 외부에서 건드리지 말라는 신호


    @property
    def age(self):      # getter 외부에 노출시킴
        return self.__age
    
    @age.setter
    def age(self, age):      # setter
        
        if age < 0:     
            raise AgeException('나이는 음수가 할당될 수 없습니다')
        self.__age = age
        

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if name == '':
            raise NameException('이름은 빈칸이 할당될 수 없습니다.')
        self.__name = name

        
    def introduce(self):
        print(f'안녕하세요, 저는 {self.name}이고, 나이는 {self.age}살 입니다.')
try:
    hong = Person('홍길동',20)
    iu = Person('아이유',20)
    lee = Person('',10)


    li = [hong,iu]
    tot = 0
    for p in li:
        tot += p.age

    print(f'우리 마을 사람들의 평균 연령: {tot/len(li)}')
except RuntimeError as e:
    print(e)

'''
정상적인 생성자 > 조건에 맞게 생성
Property
-getter > 읽어들이기
-setter > 조건에 맞게 변경하기
'''