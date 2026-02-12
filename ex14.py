'''
file

text file
binary file

open(파일 경로, 오픈모드, [인코딩 옵션])
close() <-- open()+close() 필수

open mode
t: text mode(default)
b: binary mode

r: 읽기모드, 파일이 없으면 에러
w: 쓰기모드, 항상 새 파일 생성
a: 추가모드, 기존 파일에 데이터 추가, 파일이 없으면 w 동작
'''

'''
# 텍스트 데이터 저장
# wt: write & text
f= open('test.txt','wt', encoding='utf-8')
f.write('안녕하세요.\n')
f.write('파이썬입니다.\n')
f.write('이것은 파이썬으로 저장한 파일입니다.\n')
f.close()

f= open('my_text.txt','rt', encoding='utf-8')
s = f.read()        # 한번에 모두 읽기
print(s)
f.close()

# 파일 닫기 자동 실행
with open('my_text.txt','rt', encoding='utf-8') as f:
    while True:

        s=f.readline()
        if s=='':       # 끝까지 다 읽음
            break
        print(s, end = '')
'''

with open('my_text.txt', 'rt', encoding='utf-8') as f:
    while True:
        s = f.read(4)       # N 글자수만큼 읽어나감
        if s=='':       
            break
        print(s, end = '')
