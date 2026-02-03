def americano(money):
    cup = int(money / 1500)
    rem = money % 1500
    return cup, rem

def totaler(until, even=True):
    '''even 변수에 따라 홀수/짝수 계산'''
    total = 0
    cmp = 0 if even else 1
    for n in range(until+1):
        if n%2 ==cmp:
            total += n
    return total

def calculator(num1:int|float, op:str, num2:int|float):
    match(op):
        case '+': return num1+num2
        case '-': return num1-num2
        case '*': return num1*num2
        case '/': return num1/num2
        case _: return print("유효하지 않은 연산입니다.")
        
        



