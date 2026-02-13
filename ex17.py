import json
lee = {
    '번호': 1,
    '이름': '이랑',
    '국어': 100,
    '수학': 90,
    '영어': 80
}

li = []
li.append(lee)

def input_student():
    stu = {}
    stu_info = ['번호', '이름', '국어', '수학', '영어']
    for i in stu_info:
        try:
            stu[i]= int(input(f"{i}를 입력하세요: "))
        except:
            stu[i]= input(f"{i}를 입력하세요: ")
        
    return stu

def save_json(data:list):
    with open ('students.json', 'wt', encoding='utf-8') as f:
        json.dump(data,f)       # data(list,dict)를 f(file)에 저장

def load_json():
    with open('students.json','rt',encoding='utf-8') as f:
        data = json.load(f)
        return data
        # for stu in data:
        #     for k,v in stu.items():
        #         print(f"{k},:{v}")
        #     print()


# 리스트 각 항목 가져와서 총점 평균 등급 구하는 함수
def calc_tot_avg(data):
    tot = data['국어']+data['영어']+data['수학']
    avg = float(tot)/3
    grade = get_grade(avg)
    return tot, avg, grade

def get_grade(score):
    match (score%10):
        case 9|10: return 'A'
        case 8: return 'B'
        case 7: return 'C'
        case _: return 'F'

def print_json_file():
        with open('students.json','rt',encoding='utf-8') as f:
            data = json.load(f)
            for stu in data:
                for k,v in stu.items():
                    print(f"{k},:{v}")
                print()


# new_stu = input_student()
# # if new_stu is not None:
# #     li.append(new_stu)

# save_json(new_stu)

# file = load_json()
# print(calc_tot_avg(file))

