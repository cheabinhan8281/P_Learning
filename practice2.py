class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_menu(self):
        print(f"메뉴명: {self.name}, 가격: {self.price}")
    
    def __str__(self):
        return f"{self.name}, {self.price}"     # 객체만 호출해도 return 전체 출력
    
def discount(self, rate):
    self.price = self.price*rate

def main():
    drink1 = Menu('아메리카노', 1500)
    dessert1 = Menu('두쫀쿠', 5500)
    menu_li = [drink1, dessert1]
    for i in menu_li:
        print(i)


if __name__ == '__main__':
    main()