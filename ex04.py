# JSON: Javascript Object Notation, 이종간의 시스템데이터를 교환하기 위해 고안된 자료구조 포맷

hong = {
    '번호': 1,
    '이름': '홍길동',
    '국어': 86,
    '영어': 90,
    '수학': 74
}
iu = {
    '번호': 2,
    '이름': '아이유',
    '국어': 86,
    '영어': 90,
    '수학': 74
}
lee = {
    '번호': 3,
    '이름': '이제훈',
    '국어': 86,
    '영어': 90,
    '수학': 74
}

students = []
students.append(hong)
students.append(iu)
students.append(lee)

print(students, len(students))

for s in students:
    # print(s['이름'])
    s['총점']= s['국어']+s['영어']+s['수학']
    s['평균']= int(s['총점']/3)
    
    print(s)

