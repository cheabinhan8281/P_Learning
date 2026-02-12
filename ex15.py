src_file = r'C:\Users\user\Documents\hcb\P_Learning.zip'
target_file = 'P_Learning.zip'
with open(src_file, 'rb') as src:           # binary 타입 인코딩 옵션 X
    with open(target_file, 'wb') as target:
        size = 256          # 한번에 읽을 데이터 양
        while True:
            buf = src.read(size)
            if not buf:     # binary 파일 끝까지 다읽음
                break
            target.write(buf)

print('파일 복사가 완료되었습니다.')