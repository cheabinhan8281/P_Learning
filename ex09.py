class Champion:
    def __init__(self, name):
        self.name = name
        self.attack = 10
        self.hp = 100
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x = x
        self.y = y
        print(f'{self.name}이 {self.x}, {self.y} 위치로 이동')

    def qskill(self, unit):
        print(f'{self.name}이 {unit.name}을 Q 스킬로 공격')

    def wskill(self, unit):
        print(f'{self.name}이 {unit.name}을 W 스킬로 공격')

    def introduce(self):    # 메소드 method
        print(f'챔피언: Champion, 이름: {self.name}, hp: {self.hp}')

    def __repr__(self):
        return f'{self.name} (HP: {self.hp}, ATK: {self.attack})'
    
    def __eq__ (self,dest):     # == 등가연산자 사용
        # dest가 비교 대상인가?
        if not isinstance(dest, Champion):
            return False    # 비교대상이 아니므로 거짓을 반환
        # 가정: 이름과 hp와 attack의 값이 완전히 동일하다면 같은 인스턴스로 보겠음
        return self.name == dest.name and \
                self.attack == dest.attack and \
                self.hp == dest.hp

# Mordekaise는 Champion으로부터 파생된 클래스
# Champion: 부모 클래스, super class
# Mordekaise: 자식 클래스, sub-class

# Mordekaise 클래스
class Mordekaise(Champion):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 200
        self.attack = 30

    # override
    def introduce(self):
        print(f'챔피언: 모데카이저, 이름: {self.name}, hp: {self.hp}')

    def rskill(self, target: Champion):
        damage = int(self.attack * 1.5)
        target.hp -= damage
        print(f'{self.name}이 {target.name}을 근거리 R 스킬로 공격 ({damage} 데미지)')


# Jin 클래스
class Jin(Champion):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 150
        self.attack = 20

    def rskill(self, target: Champion):
        damage = int(self.attack * 1.5)
        target.hp -= damage
        print(f'{self.name}이 {target.name}을 원거리 R 스킬로 공격 ({damage} 데미지)')


if __name__ == '__main__':
    sj = Mordekaise('sj의 모데카이저')
    sj.move(10, 10)

    hong = Jin('hong의 진')
    hong.move(10, 10)

    sj.wskill(hong)
    hong.rskill(sj)

    sj.introduce()
    hong.introduce()

    lee = Jin('Lee의 진')
    kim = Jin('Kim의 진')
    kim2 = Jin('Kim의 진')

    if lee == kim:
        print("둘이 같음")
    else:
        print("둘이 다름")



    num = 10
    li = [1,2,3]
    num.__repr__

    ###
