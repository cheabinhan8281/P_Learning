'''
문자열 데이터와 문자열 데이터의 길이를 갖는 딕셔너리 정의
'''
import json

{
    "문자열":"안녕하세요",
    "len":5
}

def str_function ():
    str_dict = {}
    s = input("문자열 입력(종료 x): ")
    if s.lower() == 'x':
        return None
    str_dict["문자열"] = s
    str_dict["len"] = len(str_dict["문자열"])
    return str_dict

def save_data(data:list):
    with open('ex18_save','wt', encoding='utf-8') as f:
        json.dump(data,f)       # data(list,dict)를 f(file)에 저장

def load_data():
    with open('ex18_save','rt',encoding='utf-8') as f:
        data = json.load(f)
        return data
    
def first_last_ch(data):
    for i in data:
        i['First'] = i['문자열'][0]
        i['Last'] = i['문자열'][-1]


def reverse_str(data):
    for i in data:
        i['reverse'] = i['문자열'][::-1]


def print_data(data):
    for i in data:
        for k,v in i.items():
            print (f'{k}:{v}')

if __name__ == "__main__":
    li = []
    # while True:
    #     str_dict = str_function()
    #     if str_dict == None:
    #         print('종료')
    #         save_data(li)
    #         data = load_data()
    #         print_data(data)
    #         exit (0)
    #     li.append(str_dict)

    data = load_data()
    first_last_ch(data)
    reverse_str(data)
    print_data(data)

    exit (0)
    print('종료')    
