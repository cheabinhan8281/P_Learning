# File Handing
# 파일: 위치(경로, path), 파일명, 확장자(Extension)
# Full Path(절대경로) ==> Path
# C:\users\user\Documents\hcb\P_Learning\ex13.py
# 

import os
#try:
#    os.mkdir('doc')        # directory 생성
#except FileExistsError:
#    os.rmdir('doc')        # directory 삭제

os.system('cls')
# 현재 디렉토리를 절대경로로 가짐
print(os.path.abspath(os.path.curdir))

curdir = os.path.abspath(os.path.curdir)
# ex01.py 파일의 절대경로
ex01 = os.path.join(curdir, 'ex01.py')
ex01_target = os.path.join(r'C:\Users\user\Desktop', 'ex01.py')

os.system(f'copy {ex01} {ex01_target}')
print()

# C:\Users\user\Desktop